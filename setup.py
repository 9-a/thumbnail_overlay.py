#!/usr/bin/env python3

from distutils.core import setup

setup(
    name = 'thumbnail_overlay',
    version = '1.0',
    description = 'Creates image thumbnails with overlays',
    author = 'Eric',
    license = 'Unlicense',
    scripts = ['thumbnail_overlay.py'],
    requires = ['PIL'],
)
