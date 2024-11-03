# afetchx

Asynchronously fetch image URLs using httpx.

`afetchx` parses command-line arguments to determine the list of image URLs to fetch, the maximum number of concurrent connections, the cooldown time between requests, an optional JSON file containing URLs, and output options. It then fetches the images, saves them in the specified output directory, and prints the number of successfully downloaded images.

[![Python Versions](https://img.shields.io/pypi/pyversions/afetchx)](https://github.com/DJStompZone/afetchx/releases/latest)

[![Python Versions](https://img.shields.io/badge/python%203.13-yes%20✅-blue)](https://github.com/DJStompZone/afetchx/releases/latest)

[![Tested on Py3.10+](https://github.com/DJStompZone/afetchx/actions/workflows/tests.yml/badge.svg)](https://github.com/DJStompZone/afetchx/actions/workflows/tests.yml)

[![Code Size](https://img.shields.io/github/languages/code-size/djstompzone/afetchx)](https://github.com/djstompzone/afetchx/releases/latest)

[![PyPI - Wheel](https://img.shields.io/pypi/wheel/afetchx)](https://pypi.org/projects/afetchx)

[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDcuNTAwMDE1MjU4Nzg5MDYiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAyMDcuNTAwMDE1MjU4Nzg5MDYgMzUiPjxyZWN0IHdpZHRoPSIxMDkuNzAxNzEzNTYyMDExNzIiIGhlaWdodD0iMzUiIGZpbGw9IiNmY2U0YmQiLz48cmVjdCB4PSIxMDkuNzAxNzEzNTYyMDExNzIiIHdpZHRoPSI5Ny43OTgzMDE2OTY3NzczNCIgaGVpZ2h0PSIzNSIgZmlsbD0iIzAwMDAwMCIvPjx0ZXh0IHg9IjU0Ljg1MDg1Njc4MTAwNTg2IiB5PSIyMS41IiBmb250LXNpemU9IjEyIiBmb250LWZhbWlseT0iJ1JvYm90bycsIHNhbnMtc2VyaWYiIGZpbGw9IiMwMDAwMDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5QSVAgSU5TVEFMTDwvdGV4dD48dGV4dCB4PSIxNTguNjAwODY0NDEwNDAwNCIgeT0iMjEuNSIgZm9udC1zaXplPSIxMiIgZm9udC1mYW1pbHk9IidNb250c2VycmF0Jywgc2Fucy1zZXJpZiIgZmlsbD0iI2U4YjY2MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjkwMCIgbGV0dGVyLXNwYWNpbmc9IjIiPkFGRVRDSFg8L3RleHQ+PC9zdmc+)](https://pypi.org/projects/afetchx)

## Usage

Invoke the script with

```bash
python -m afetchx {args}
```

## Command-line arguments

- `-n`, `--max_connections`: Max number of concurrent connections (default: 5).
- `-c`, `--cooldown`: Cooldown time between requests in seconds (default: 1.0).
- `-j`, `--json`: Path to a JSON file containing URLs to fetch.
- `-o`, `--output-dir`: Directory to save downloaded images (default: `./downloaded` in the current working directory).
- `--filename-format`: Lambda function as a string to format filenames based on the URL (e.g., `"lambda url: url.split('/')[-1].split('.')[0] + '.png'"`).
- `urls`: List of image URLs to fetch (positional arguments).

### *Note*: You must satisfy exactly one of the following conditions

1. Use the `--json` (`-j`) argument to specify a JSON file containing URLs.
2. Provide one or more URLs directly as positional arguments.

## Examples

### Basic Usage

Download images from a JSON file with a cooldown of 1 second between each download and a maximum of 5 concurrent connections:

```bash
python -m afetchx -j urls.json -c 1.0 -n 5
```

### Specify Output Directory

Download images from URLs provided as positional arguments and save them to a custom directory:

```bash
python -m afetchx -c 1.0 -n 5 -o ./downloaded_pictures "https://unsplash.it/256.jpg" "https://unsplash.it/512.jpg"
```

### Use Custom Filename Format

Download images and apply a custom filename format based on the URL:

```bash
python -m afetchx -c 1.0 -n 5 --filename-format "lambda url: url.split('/')[-1].split('.')[0] + '.png'" "https://example.com/image1.png" "https://example.com/image2.jpg"
```

In this example, each downloaded image will be named according to the lambda function. The filename format option can be especially useful for sanitizing or modifying filenames before saving.

## Error Handling

If both URLs and a JSON file are provided, the script will print an error and exit. Likewise, if neither URLs nor a JSON file are provided, the script will print an error and exit. Ensure exactly one source for URLs.
