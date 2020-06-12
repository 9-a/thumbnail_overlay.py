#!/usr/bin/env python3

import argparse
import glob
import os
from PIL import Image

def _thumbnail_max(img, size):
    """Similar to Image.thumbnail, but resizes the given image
    such that it is no SMALLER than the given size, and it
    returns a new image instead of modifying the original"""

    W, H = size
    w, h = img.size
    ratio = w / h

    if w > h:
        H = round(W / ratio)
    else:
        W = round(H * ratio)

    return img.resize((W, H), Image.ANTIALIAS)

def _crop_center(img, size):
    """Crops an image to a given size from its center"""

    W, H = size
    w, h = img.size
    return img.crop((
        (w - W) / 2,
        (h - H) / 2,
        (w + W) / 2,
        (h + H) / 2
    ))

def make_thumbnail(img, overlay):
    """ Resize a given image to the overlay size,
    and apply the overlay"""

    img = _thumbnail_max(img, overlay.size)
    img = _crop_center(img, overlay.size)
    img.paste(overlay, mask = overlay)

    return img

def _main(background_path, overlay_path, output_dir):
    overlay = Image.open(overlay_path)

    for file in glob.iglob(background_path):
        img = Image.open(file)
        img = make_thumbnail(img, overlay)
        img.save(os.path.join(output_dir, os.path.basename(file)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Creates image thumbnails with overlays')
    parser.add_argument('background',   type = str, help = 'background image(s)')
    parser.add_argument('overlay',      type = str, help = 'overlay image')
    parser.add_argument('output_dir',   type = str, help = 'output directory')

    args = parser.parse_args()
    _main(args.background, args.overlay, args.output_dir)
