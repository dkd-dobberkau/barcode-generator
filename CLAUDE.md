# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains three Python CLI tools for code generation:
1. **EAN-13 Barcode Generator** (`ean13_generator.py`) - Generates EAN-13 barcodes in SVG or PNG format
2. **QR Code Generator** (`qr_generator.py`) - Generates QR codes with customizable options
3. **Multi-Format Barcode Generator** (`barcode_generator.py`) - Generates 12+ barcode types using treepoem

## Setup and Dependencies

Install Ghostscript first (required for treepoem):
- macOS: `brew install ghostscript`
- Ubuntu/Debian: `sudo apt-get install ghostscript`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tools

### EAN-13 Barcode Generator
```bash
# Generate SVG barcode (default format)
./ean13_generator.py 123456789012

# Generate PNG barcode with custom output name
./ean13_generator.py 123456789012 -f png -o my_barcode

# Show help
./ean13_generator.py --help
```

### QR Code Generator
```bash
# Generate basic QR code
./qr_generator.py "Hello World"

# Generate customized QR code
./qr_generator.py "https://example.com" -f svg -e H --box-size 15 --fill-color red

# Show help
./qr_generator.py --help
```

### Multi-Format Barcode Generator
```bash
# List all available barcode types
./barcode_generator.py --list-types

# Code 128 for shipping
./barcode_generator.py "SHIP123" code128

# Data Matrix for manufacturing
./barcode_generator.py "PART001" datamatrix

# PDF417 with options
./barcode_generator.py "Document" pdf417 --options "columns=3"
```

## Code Structure

- `ean13_generator.py` - EAN-13 barcode CLI with validation and format options
- `qr_generator.py` - QR code CLI with error correction, colors, and sizing options
- `barcode_generator.py` - Multi-format CLI using treepoem for 12+ barcode types
- `requirements.txt` - Dependencies for python-barcode, qrcode, and treepoem libraries
- EAN-13 tool validates input and automatically calculates checksum digit
- QR tool supports error correction levels (L/M/Q/H), custom colors, and box sizing
- Multi-format tool supports Code 128, Data Matrix, PDF417, Aztec, and more