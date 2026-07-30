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
index.html          the report
assets/styles.css   specimen-sheet styling, day + night modes
assets/app.js       plate viewer, keyboard/swipe navigation, mode toggle
photos/             eight plates, 2000px long edge
photos/thumbs/      eight thumbnails, 800px long edge
```

## A note on the photographs

Every image in this repository has been stripped of embedded metadata before commit:

- EXIF removed in full — device make and model, firmware build strings, subsecond
  timestamps, exposure data, `ImageUniqueID`
- GPS block removed. (For the record, the coordinates were null in all eight originals —
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

## Consent

The subject has reviewed the survey and consented to its publication. She would like it
noted that she was resting her eyes.
