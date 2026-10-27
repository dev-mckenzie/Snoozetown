#!/usr/bin/env python3
"""Check the navigator data and build the single-file page.

Usage:
  python3 build.py DATA_DIR --check          check the data only
  python3 build.py DATA_DIR OUTPUT.html      check, then build the page
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = ["programs", "pathways", "appeals", "alerts", "glossary", "counties", "meta"]
CATEGORIES = {"start", "dd", "health", "money", "school", "work", "decisions", "home",
              "housing", "transport", "equipment", "sensory", "rights"}
QUESTIONS = {
    "county": None, "age": "number",
    "dis": {"idd", "physical", "deaf", "blind", "tbi", "mh", "unsure"},
    "onset22": {"yes", "no", "unsure"},
    "dd_elig": {"yes", "applied", "no", "unsure"},
    "waiver": {"yes", "waiting", "no", "unsure"},
    "mhn": {"yes", "applied", "no", "unsure"},
    "ssa": {"ssi", "ssdi", "cdb", "none", "unsure"},
    "school": {"iep", "504", "none_in_school", "left", "unsure"},
    "work": {"working", "wants", "no", "unsure"},
    "daily": {"yes", "no", "unsure"}, "nursing": {"yes", "no", "unsure"},
    "caregiver55": {"yes", "no", "unsure"}, "caregiver_risk": {"yes", "no", "unsure"},
    "guardian": {"has", "considering", "no", "unsure"},
    "needs": {"transport", "housing", "equipment", "respite", "money", "job"},
    "resources_over": {"yes", "no", "unsure"},
}
OPS = {"==", "!=", ">=", "<=", ">", "<", "in", "has", "lacks"}
# A dash is allowed only between two digits (a range like 16–25).
BAD_DASH = re.compile(r"—|(?<!\d)–|–(?!\d)")

errors, warnings = [], []


def walk_strings(obj, path):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")


def check_rule(rule, where, counties):
    if rule is True or rule is None:
        return
    if not isinstance(rule, dict):
        errors.append(f"{where}: rule must be an object, true, or null")
        return
    for key in ("all", "any"):
        if key in rule:
            for i, r in enumerate(rule[key]):
                check_rule(r, f"{where}.{key}[{i}]", counties)
            return
    if "not" in rule:
        check_rule(rule["not"], f"{where}.not", counties)
        return
    q, op, v = rule.get("q"), rule.get("op"), rule.get("v")
    if q not in QUESTIONS:
        errors.append(f"{where}: unknown question id {q!r}")
        return
    if op not in OPS:
        errors.append(f"{where}: unknown op {op!r}")
    allowed = QUESTIONS[q]
    if q == "county":
        allowed = set(counties) | {"other", "unsure"}
    if allowed == "number":
        if not isinstance(v, (int, float)):
            errors.append(f"{where}: age needs a number")
        return
    for x in (v if isinstance(v, list) else [v]):
        if x not in allowed:
            errors.append(f"{where}: value {x!r} is not valid for {q}")


MERGED = ("programs", "glossary")  # these may be split into programs-a.json, programs-b.json, ...


def load(data_dir):
    data = {}
    for name in MERGED:
        parts = sorted(data_dir.glob(f"{name}*.json"))
        if not parts:
            errors.append(f"missing file {name}.json (or {name}-*.json)")
        merged = []
        for f in parts:
            try:
                merged += json.loads(f.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errors.append(f"{f.name}: invalid JSON: {e}")
        if name == "glossary":
            terms = {}
            for t in merged:
                terms.setdefault(t.get("term", "").strip().lower(), t)
            merged = list(terms.values())
        data[name] = merged
    for name in FILES:
        if name in MERGED:
            continue
        f = data_dir / f"{name}.json"
        if not f.exists():
            errors.append(f"missing file {f.name}")
            data[name] = {} if name == "meta" else []
            continue
        try:
            data[name] = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: invalid JSON: {e}")
            data[name] = {} if name == "meta" else []
    return data


def check(data):
    counties = [c.get("id") for c in data["counties"]]
    ids = [p.get("id") for p in data["programs"]]
    seen = set()
    for i in ids:
        if i in seen:
            errors.append(f"duplicate program id {i!r}")
        seen.add(i)
    for p in data["programs"]:
        w = f"programs[{p.get('id')}]"
        for field in ("id", "name", "category", "order", "summary", "checked", "sources"):
            if field not in p:
                errors.append(f"{w}: missing {field}")
        if p.get("category") not in CATEGORIES:
            errors.append(f"{w}: bad category {p.get('category')!r}")
        for r in p.get("requires", []):
            if r not in seen:
                errors.append(f"{w}: requires unknown id {r!r}")
        if "rule" in p:
            check_rule(p["rule"], f"{w}.rule", counties)
        else:
            errors.append(f"{w}: missing rule (use null for guide only)")
        if "have" in p:
            check_rule(p["have"], f"{w}.have", counties)
        cs = p.get("counties", "all")
        if cs != "all":
            for c in cs:
                if c not in counties:
                    errors.append(f"{w}: unknown county {c!r}")
        for c in p.get("contacts", []):
            for cc in ([] if c.get("counties", "all") == "all" else c["counties"]):
                if cc not in counties:
                    errors.append(f"{w}: contact {c.get('label')!r} has unknown county {cc!r}")
            if c.get("url") and not c["url"].startswith("https://"):
                warnings.append(f"{w}: contact url is not https: {c['url']}")
        if p.get("confidence") not in ("High", "Medium", "Low"):
            warnings.append(f"{w}: confidence should be High, Medium, or Low")
    for wy in data["pathways"]:
        w = f"pathways[{wy.get('id')}]"
        if "rule" in wy:
            check_rule(wy["rule"], f"{w}.rule", counties)
        for i, s in enumerate(wy.get("steps", [])):
            for r in s.get("programs", []):
                if r not in seen:
                    errors.append(f"{w}.steps[{i}]: unknown program {r!r}")
    for al in data["alerts"]:
        for r in al.get("programs", []):
            if r not in seen:
                errors.append(f"alerts[{al.get('id')}]: unknown program {r!r}")
    for name in FILES:
        for path, s in walk_strings(data[name], name):
            if BAD_DASH.search(s):
                errors.append(f"{path}: dash used as punctuation: {s[:80]!r}")


def build(data, out):
    template = (HERE / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = template.replace("__DATA__", payload, 1)
    Path(out).write_text(html, encoding="utf-8")
    print(f"built {out} ({len(html) // 1024} KB, {len(data['programs'])} programs)")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    data = load(Path(sys.argv[1]))
    check(data)
    for w in warnings:
        print("WARNING", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    if errors:
        sys.exit(1)
    if sys.argv[2] != "--check":
        build(data, sys.argv[2])


if __name__ == "__main__":
    main()
