# QR Code Generator

A simple Python project to generate QR codes from user input.

## Description

This repository contains a lightweight Python script that creates QR code images from a URL or text input. The generated QR code is saved as a PNG file.

## Features

- Generates QR codes from custom input
- Saves the QR code image as a `.png` file
- Automatically appends `.png` to the filename if omitted

## Requirements

- Python 3.x
- `qrcode` Python package

## Installation

1. Install Python 3 if it is not already installed.
2. Install the required package:

```bash
pip install qrcode[pil]
```

## Usage

Run the script from the project folder:

```bash
python "QR Code Generator/main.py"
```

Follow the prompts:

1. Enter the URL or text to encode.
2. Enter the filename for the generated QR code image.

Example:

```text
Enter your url: https://example.com
Filename you want to save it as: my_qrcode
```

The output file will be saved as `my_qrcode.png`.

## Project Structure

- `QR Code Generator/main.py` - main Python script that generates the QR code.
- `QR Code Generator/my_github.png` - example image file included in the folder.

