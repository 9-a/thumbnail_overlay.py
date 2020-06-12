# thumbnail.py

Automatically generate thumbnails from images.

For each file in an input directory, ``thumbnail.py`` resizes it to the dimensions of an overlay image, pastes the overlay on top of the source image, and saves it to an output directory, with the same filename.

# Usage
```
usage: thumbnail.py [-h] background overlay output_dir

Automatically generate thumbnails

positional arguments:
  background  background image(s)
  overlay     overlay image
  output_dir  output directory

optional arguments:
  -h, --help  show this help message and exit
```
