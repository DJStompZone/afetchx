<div align="center">
  <h1>afetchx</h1>
<img src="https://github.com/user-attachments/assets/8539b847-9bfd-4388-ac8b-384d64281d8a" width="40%">
  <h3>Asynchronously fetch image URLs using httpx.</h3>
</div>

<hr>

## Overview

`afetchx` parses command-line arguments to determine the list of image URLs to fetch, the maximum number of concurrent connections, the cooldown time between requests, an optional JSON file containing URLs, and output options. It then fetches the images, saves them in the specified output directory, and prints the number of successfully downloaded images.

[![Python Versions](https://img.shields.io/pypi/pyversions/afetchx)](https://github.com/DJStompZone/afetchx/releases/latest)

[![Python Versions](https://img.shields.io/badge/python%203.13-yes%20✅-blue)](https://github.com/DJStompZone/afetchx/releases/latest)

[![Tested on Py3.10+](https://github.com/DJStompZone/afetchx/actions/workflows/tests.yml/badge.svg)](https://github.com/DJStompZone/afetchx/actions/workflows/tests.yml)

[![Code Size](https://img.shields.io/github/languages/code-size/djstompzone/afetchx)](https://github.com/djstompzone/afetchx/releases/latest)

[![PyPI - Wheel](https://img.shields.io/pypi/wheel/afetchx)](https://pypi.org/projects/afetchx)

## Installation

<a href="https://pypi.org/projects/afetchx"><img src="https://github.com/user-attachments/assets/471667e2-bd29-47b0-b414-055c21740040" height="30px"></a>

Or

<a href="https://github.com/DJStompZone/afetchx/archive/refs/heads/master.zip"><img src="https://github.com/user-attachments/assets/86df3959-e061-4e18-9603-3fa805b4a31e" height="30px"></a>

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
