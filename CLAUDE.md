# Snoozetown

A static site. Field Report No. 1: a survey of Ro asleep, written in the register of a
scientific field study.

## Writing rules

**Never use the em dash (—) in any text.** This applies to everything: site copy, README,
code comments, commit messages, and pull request descriptions. Restructure the sentence
instead. A colon, a semicolon, a comma, parentheses, or a full stop will do the job.

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
