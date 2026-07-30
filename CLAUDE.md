# Snoozetown

A static site. Field Report No. 1: a survey of Ro asleep, written in the register of a
scientific field study.

## Writing rules

**Never use a dash as punctuation.** No em dashes (—) in site copy, README, code comments,
commit messages, or pull request descriptions. Restructure the sentence instead. A colon, a
semicolon, a comma, parentheses, or a full stop will do the job.

The one exception: a dash **inside a date or number range** is fine, and there are two in
the site already (`27 Mar 2022 – 3 Aug 2025` in the masthead, `2022–2025` in the meta
description). Leave them alone. If you find a dash anywhere that is not spanning a range,
it is a mistake and should be rewritten out.

Other conventions for site copy:

- The voice is deadpan scientific. Play it completely straight. The humour comes from the
  register, never from winking at the reader. No exclamation marks, no "haha", no asides
  about how funny this is.
- The subject is called **Ro**. Never her full name.
- Capture times are given to the second, because the precision is the joke.
- Field notes describe only what is visible in the photograph. Do not invent detail.

## Photographs

Every image published here must be stripped of metadata before it is committed. Use
`tools/add-specimen.py`, which reads the capture timestamp, removes all EXIF, bakes the
orientation flag into the pixels, resizes, and verifies the result.

Original camera files must never be committed. `.gitignore` covers the usual cases, but
check before staging.

## Structure

No build step, no dependencies, no framework. `index.html` plus one stylesheet and one
script. The page must remain fully readable with JavaScript disabled; the plate viewer and
the night mode toggle are enhancements, not requirements.

Sections are numbered (§1 Abstract, §2 Catalogue, and so on). If you add a section,
renumber the rest and check the `.findings` counter prefix in the stylesheet, which is
hardcoded to `4.` for §4.
