# Data format for the navigator site

The navigator site has two parts that share one data set:
1. A screener: the caregiver answers questions, the page shows programs and next steps.
2. A guide: program cards, pathways by age and need, an appeals table, and a glossary.

Every text field has two levels: `plain` for caregivers, `pro` for professionals.
Plain text: short sentences, active voice, simple words (ASD-STE100 style), maximum about
20 words per sentence. Pro text: exact rules, numbers, citations.

NO em dashes or en dashes as punctuation anywhere. A dash inside a number range (16–25) is fine.

Use ONLY facts from the team files (01 to 08) as corrected by the fact checks (09, 09b).
If a fact check says "corrected", use the corrected fact. If a fact is "could not verify",
either leave it out or mark the record `"confidence": "Low"` and say "call to confirm" in the
plain text. NEVER include a phone number, address, or URL that a fact check marked wrong.

All files are JSON, UTF-8, valid (check with `python3 -m json.tool <file>`).

## Screener questions (fixed; rules may use only these ids and values)

| id | type | values |
|---|---|---|
| `county` | select | one of the 23 county names in the region (lowercase, for example `greene`, `christian`, `jasper`), or `other` |
| `age` | number | years |
| `dis` | multi | `idd` (intellectual or developmental disability, including autism and cerebral palsy), `physical` (physical disability or complex medical needs), `deaf` (Deaf or hard of hearing), `blind` (blind or low vision), `tbi` (brain injury), `mh` (mental health condition) |
| `onset22` | single | `yes`, `no`, `unsure` (did the disability start before age 22) |
| `dd_elig` | single | `yes`, `applied`, `no`, `unsure` (has DMH DD eligibility) |
| `waiver` | single | `yes`, `waiting`, `no`, `unsure` (has a DD waiver now) |
| `mhn` | single | `yes`, `applied`, `no`, `unsure` (has MO HealthNet / Medicaid) |
| `ssa` | multi | `ssi`, `ssdi`, `cdb` (Childhood Disability Benefits on a parent's record), `none`, `unsure` |
| `school` | single | `iep`, `504`, `none_in_school`, `left` (in school with an IEP, in school with a 504 plan, in school with neither, left school) |
| `work` | single | `working`, `wants`, `no` |
| `daily` | single | `yes`, `no` (needs hands-on help with daily care such as bathing, dressing, eating) |
| `nursing` | single | `yes`, `no` (needs skilled nursing, for example a trach, ventilator, or tube feeding) |
| `caregiver55` | single | `yes`, `no` (main unpaid caregiver is 55 or older) |
| `caregiver_risk` | single | `yes`, `no` (the caregiver is ill, cannot continue, or has died) |
| `guardian` | single | `has`, `considering`, `no` (legal guardian status, for a person 17 or older) |
| `needs` | multi | `transport`, `housing`, `equipment`, `respite`, `money`, `job` |
| `resources_over` | single | `yes`, `no`, `unsure` (the person has more than the MO HealthNet resource limit in savings or property) |

Every single-choice question also accepts `unsure`, and the multi-choice questions `dis` and
`ssa` accept `unsure` too. The screener never tells a person "not eligible". Programs that do
not match stay visible in a "Programs to check with a professional" list.

## Rule format

A rule is a JSON object. The engine supports:
- `{"q":"age","op":">=","v":18}` with op one of `==`, `!=`, `>=`, `<=`, `>`, `<`
- `{"q":"mhn","op":"in","v":["yes","applied"]}` (single value is one of the list)
- `{"q":"dis","op":"has","v":["idd","tbi"]}` (multi answer includes at least one)
- `{"q":"dis","op":"lacks","v":["idd"]}` (multi answer includes none)
- `{"all":[ ...rules ]}`, `{"any":[ ...rules ]}`, `{"not": rule}`
- `true` (always matches)

An answer of `unsure` or a blank answer makes a match "maybe" instead of "likely". The engine
handles this. Write rules for the clear case.

## File: programs.json

An array of program records:

```json
{
  "id": "dmh-dd-eligibility",
  "name": "DMH Developmental Disabilities eligibility",
  "category": "dd",
  "order": 10,
  "summary": {"plain": "One sentence: what it is and why it matters.", "pro": "One sentence for a professional."},
  "who": {"plain": "Who can get it.", "pro": "Exact eligibility rules with numbers and year."},
  "steps": {"plain": ["Step 1.", "Step 2."], "pro": ["Detailed step with form names."]},
  "bring": ["Document 1", "Document 2"],
  "wait": {"plain": "How long it takes.", "pro": "Rule-based time limits."},
  "cost": "Free",
  "watch_out": {"plain": ["Common reason people get stuck."], "pro": ["Detail."]},
  "appeal": {"plain": "What to do if denied, with the deadline.", "pro": "Appeal rule and citation."},
  "alert": "Optional. A current system problem with a date, for example a wait list. Empty string if none.",
  "requires": ["ids of programs that must come first"],
  "rule": {"all":[{"q":"onset22","op":"in","v":["yes"]},{"q":"dis","op":"has","v":["idd","physical","tbi","deaf","blind"]}]},
  "counties": "all",
  "contacts": [
    {"label": "Springfield Regional Office", "phone": "417-000-0000", "url": "https://...", "address": "...", "counties": "all"}
  ],
  "sources": [{"title": "...", "url": "https://..."}],
  "confidence": "High",
  "checked": "2026-10-27"
}
```

`category` is one of: `start` (front doors), `dd` (DMH DD system and waivers), `health`
(MO HealthNet and health care), `money` (SSI, SSDI, CDB, ABLE, trusts, work incentives),
`school` (school and transition), `work` (VR and employment), `decisions` (guardianship and
alternatives), `home` (home care, respite, caregiver support), `housing`, `transport`,
`equipment`, `sensory`, `rights` (advocacy, protection and advocacy, legal help).

`order` is a number. Lower numbers appear first. Use it to put prerequisites first.
`counties` is `"all"` or an array of county ids where the program exists.
Contacts may have their own `counties` list, so the page can show the right local office.
`rule` may be `true` for "everyone should know this". Programs with `"rule": null` appear in
the guide only, not in screener results.

### Shared program ids

Two data agents write programs at the same time (`programs-a.json` and `programs-b.json`). To
link to a program in the other file (in `requires`, pathway steps, or alerts), use ONLY these
shared ids. Each id must exist in the file of the agent that owns it.

Owned by agent A: `first-call-dmh-intake`, `dmh-dd-eligibility`, `dd-support-coordination`,
`dd-waiver-comprehensive`, `dd-waiver-community-support`, `dd-waiver-pfh`, `mo-healthnet`,
`ssi`, `ssdi`, `cdb`, `able-account`, `guardianship`, `supported-decision-making`,
`protection-advocacy`.

Owned by agent B: `dhss-home-care`, `consumer-directed-services`, `vocational-rehab`,
`pre-ets`, `iep-transition`, `paratransit-springfield`, `oats-transit`, `medicaid-rides`,
`aaa-caregiver-respite`, `missouri-assistive-technology`.

`have` is an optional rule: if it is true, the person already has this program (for example
`{"q":"mhn","op":"in","v":["yes"]}` for `mo-healthnet`).

### Check your work

Run `python3 /tmp/claude-0/-home-user-Snoozetown/898057f6-f868-5a37-83ee-038867ed6b7b/scratchpad/build/build.py <data folder> --check`.
It checks JSON, ids, rules, counties, and dashes. Fix every ERROR. Shared ids owned by the
other agent show as errors until both files exist; ignore only those.

## File: pathways.json

Step-by-step plans for key moments. An array of:

```json
{
  "id": "turning-18",
  "title": "Turning 17 and 18",
  "when": {"plain": "When to start.", "pro": "Detail."},
  "rule": {"all":[{"q":"age","op":">=","v":16},{"q":"age","op":"<=","v":19}]},
  "steps": [
    {"age": "17", "plain": "Do this.", "pro": "Detail and citation.", "programs": ["program-id"], "deadline": "Optional exact deadline text"}
  ],
  "warnings": {"plain": ["..."], "pro": ["..."]}
}
```

Required pathways: `start-here` (the first calls for any family), `turning-14-16` (transition
planning starts), `turning-18`, `leaving-school`, `turning-21` (the health care and service
cliff), `turning-22-26`, `starting-work`, `waiting-for-waiver` (what to do while on the DD wait
list), `caregiver-cannot-continue` (emergency and future planning), `when-denied` (appeal steps).

## File: appeals.json

An array of: `{"agency": "", "decision": "", "deadline": "", "keep_benefits": "", "first_step": "", "source": {"title":"","url":""}, "confidence": ""}`
Keep `deadline` and `keep_benefits` exact. These are the most dangerous facts in the data set.

## File: alerts.json

Current system problems that change what a family should do. An array of:
`{"id":"", "date":"2026-10-15", "title":"", "plain":"", "pro":"", "programs":["ids"], "source":{"title":"","url":""}}`

## File: glossary.json

An array of `{"term":"", "plain":"", "pro":""}`. Include every acronym used in the data.

## File: counties.json

An array of `{"id":"greene", "name":"Greene", "office":"Springfield Regional Office" or "Joplin Satellite Office", "sb40":"board name or empty", "notes":""}` for the 23 counties.
