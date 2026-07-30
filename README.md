# Snoozetown

A static site. Field Report No. 1: *A Longitudinal Photographic Survey of Ro at Rest.*

Eight documented instances of unscheduled daytime sleep, recorded between March 2022 and
August 2025. Population: one. Subjects woken: zero.

## Running it

There is no build step, no dependencies, and no framework. Open `index.html` in a browser,
or serve the directory:

```sh
python3 -m http.server 8000
```

## Publishing to GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → pick the branch, folder `/ (root)`.
The site is entirely static and will work as-is.

## Layout

```
index.html              the report
assets/styles.css       specimen-sheet styling, day + night modes
assets/app.js           plate viewer, keyboard/swipe navigation, mode toggle
photos/                 eight plates, 2000px long edge
photos/thumbs/          eight thumbnails, 800px long edge
tools/add-specimen.py   intake: strip metadata, resize, emit catalogue markup
CLAUDE.md               house style, including the no em dash rule
```

## Adding a specimen

Point the intake tool at the original camera files. It reads the capture timestamp,
removes every trace of metadata, bakes in the orientation, writes the plate and the
thumbnail at the next free number, verifies the result is clean, and prints a catalogue
entry with the date and time already filled in:

```sh
python3 tools/add-specimen.py ~/Pictures/IMG_5001.jpg
```

Paste the printed block into the `<ol class="catalogue">` in `index.html`, keeping the
catalogue in chronological order, then fill in the substrate, posture, apparatus and field
note. Update the specimen count in the masthead. The originals stay wherever they are; the
tool never copies them into the repository.

## A note on the photographs

Every image in this repository has been stripped of embedded metadata before commit:

- EXIF removed in full: device make and model, firmware build strings, subsecond
  timestamps, exposure data, `ImageUniqueID`
- GPS block removed. (For the record, the coordinates were null in all eight originals;
  location services were off at capture, so nothing was ever written.)
- Images re-encoded from raw pixel data rather than resaved, so no metadata can survive
  in the container. Only the JFIF density header remains, which carries nothing.
- EXIF orientation flags resolved into the pixels themselves, so the photos display
  upright everywhere regardless of viewer support.

Verify at any time:

```sh
python3 -c "from PIL import Image; import glob; \
print({f: len(dict(Image.open(f).getexif())) for f in glob.glob('photos/**/*.jpg', recursive=True)})"
```

Every value should be `0`.

The original camera files are deliberately **not** in this repository, and `.gitignore`
is set up to keep it that way. Capture timestamps were transcribed by hand into the
captions before stripping, because they are the most interesting part of the data.

## Discoverability

The site is meant to be shared by link rather than found by search. Two things ask
crawlers to stay away:

- `robots.txt` disallows everything
- `index.html` carries `<meta name="robots" content="noindex, nofollow, noarchive,
  noimageindex">`, which also keeps the photographs out of image search

Both are requests, not enforcement. Well behaved crawlers honour them; nothing stops a
determined one, and anyone with the URL can still read the site. Note also that this
repository is public, which is what makes free GitHub Pages work, so the images remain
reachable through GitHub itself regardless of these settings. Making the repository
private would close that gap, but Pages on a private repository requires a paid plan.

## Consent

The subject has reviewed the survey and consented to its publication. She would like it
noted that she was resting her eyes.
