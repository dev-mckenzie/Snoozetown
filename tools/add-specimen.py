#!/usr/bin/env python3
"""Add photographs to the Snoozetown catalogue.

Reads the capture timestamp out of each file, strips every trace of metadata,
bakes in the orientation, writes a plate and a thumbnail, and prints a ready to
paste HTML block with the timestamp already filled in.

The originals are never copied into the repository.

    python3 tools/add-specimen.py ~/Pictures/IMG_5001.jpg ~/Pictures/IMG_5002.jpg

Requires Pillow:  pip install Pillow
"""

import os
import sys
from datetime import datetime

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required.  Install it with:  pip install Pillow")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PHOTOS = os.path.join(REPO, "photos")
THUMBS = os.path.join(PHOTOS, "thumbs")

FULL_MAX, THUMB_MAX, QUALITY = 2000, 800, 82

DATETIME_ORIGINAL = 0x9003
EXIF_IFD = 0x8769


def next_index():
    """Highest sleep-NN.jpg already in photos/, plus one."""
    n = 0
    for name in os.listdir(PHOTOS):
        if name.startswith("sleep-") and name.endswith(".jpg"):
            try:
                n = max(n, int(name[6:-4]))
            except ValueError:
                pass
    return n + 1


def read_timestamp(im):
    """Capture time, read before we destroy it. Returns (date, time) strings."""
    exif = im.getexif()
    raw = exif.get(306)  # DateTime on the base IFD
    try:
        ifd = exif.get_ifd(EXIF_IFD)
        raw = ifd.get(DATETIME_ORIGINAL, raw)  # prefer DateTimeOriginal
    except Exception:
        pass
    if not raw:
        return None, None
    try:
        dt = datetime.strptime(str(raw), "%Y:%m:%d %H:%M:%S")
    except ValueError:
        return None, None
    day = dt.strftime("%d %B %Y").lstrip("0")
    return day, dt.strftime("%H:%M:%S")


def scrub(im):
    """Bake orientation into pixels, then rebuild the image so that no metadata
    can survive in the container."""
    im = ImageOps.exif_transpose(im).convert("RGB")
    clean = Image.new("RGB", im.size)
    clean.paste(im)
    return clean


def process(path, index):
    slug = "sleep-%02d" % index
    src = Image.open(path)
    day, clock = read_timestamp(src)
    clean = scrub(src)

    sizes = {}
    for maxdim, folder in ((FULL_MAX, PHOTOS), (THUMB_MAX, THUMBS)):
        c = clean.copy()
        c.thumbnail((maxdim, maxdim), Image.LANCZOS)
        out = os.path.join(folder, slug + ".jpg")
        c.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        sizes[folder] = c.size

    # verify before reporting success
    check = Image.open(os.path.join(PHOTOS, slug + ".jpg"))
    remaining = len(dict(check.getexif()))
    status = "clean" if remaining == 0 else "FAILED, %d tags remain" % remaining

    w, h = sizes[THUMBS]
    print("\n%s  <-  %s" % (slug, os.path.basename(path)))
    print("  metadata: %s" % status)
    print("  captured: %s" % (("%s, %s" % (day, clock)) if day else "no timestamp found"))
    print("""
  Paste into index.html, inside <ol class="catalogue">:

      <li class="specimen" id="ST-%03d">
        <figure>
          <button class="plate" type="button" data-full="photos/%s.jpg" data-index="%d">
            <img src="photos/thumbs/%s.jpg" width="%d" height="%d" loading="lazy" decoding="async"
                 alt="DESCRIBE THE PHOTOGRAPH FOR SCREEN READERS">
          </button>
          <figcaption>
            <p class="desig">ST-%03d</p>
            <dl class="fields">
              <div><dt>Date</dt><dd>%s</dd></div>
              <div><dt>Time</dt><dd>%s</dd></div>
              <div><dt>Substrate</dt><dd>?</dd></div>
              <div><dt>Posture</dt><dd>?</dd></div>
              <div><dt>Apparatus</dt><dd>?</dd></div>
            </dl>
            <p class="note">FIELD NOTE.</p>
          </figcaption>
        </figure>
      </li>
""" % (index, slug, index - 1, slug, w, h, index, day or "?", clock or "?"))


def main(paths):
    if not paths:
        sys.exit(__doc__)
    os.makedirs(THUMBS, exist_ok=True)
    i = next_index()
    for p in paths:
        if not os.path.isfile(p):
            print("skipping, not a file: %s" % p)
            continue
        process(p, i)
        i += 1
    print("Remember to update the specimen count in the masthead and §3, "
          "and keep the catalogue in chronological order.")


if __name__ == "__main__":
    main(sys.argv[1:])
