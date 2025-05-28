# Code Generators

A collection of Python CLI tools for generating barcodes and QR codes.

## Features

### EAN-13 Barcode Generator
- Generate EAN-13 barcodes from 12-digit codes
- Automatic checksum calculation
- SVG and PNG output formats
- Input validation

### QR Code Generator
- Generate QR codes from any text or data
- Multiple error correction levels (L, M, Q, H)
- Customizable colors and sizing
- SVG and PNG output formats
- Support for URLs, text, contact info, etc.

### Multi-Format Barcode Generator
- Support for 12+ barcode types including Code 128, Data Matrix, PDF417
- Linear and 2D barcode formats
- Industry-standard encoding options
- Automatic format validation
- PNG output with professional styling

## Installation

1. Clone or download this repository
2. Install Ghostscript (required for treepoem):
   - **macOS**: `brew install ghostscript`
   - **Ubuntu/Debian**: `sudo apt-get install ghostscript`
   - **Windows**: Download from [Ghostscript website](https://www.ghostscript.com/download/gsdnld.html)
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### EAN-13 Barcode Generator

Generate EAN-13 barcodes from 12-digit codes:

```bash
# Basic usage (SVG output)
./ean13_generator.py 123456789012

# PNG output with custom filename
./ean13_generator.py 123456789012 -f png -o my_barcode

# Show help
./ean13_generator.py --help
```

**Options:**
- `-o, --output`: Output filename (default: barcode)
- `-f, --format`: Output format - svg or png (default: svg)

### QR Code Generator

Generate QR codes with extensive customization options:

```bash
# Basic usage
./qr_generator.py "Hello World"

# Generate QR code for a website
./qr_generator.py "https://example.com" -o website_qr

# Customized QR code with high error correction
./qr_generator.py "Important Data" -f svg -e H --box-size 15

# Colored QR code
./qr_generator.py "Colorful" --fill-color red --back-color yellow

# Show help
./qr_generator.py --help
```

### Multi-Format Barcode Generator

Generate various barcode types for different industries:

```bash
# List available barcode types
./barcode_generator.py --list-types

# Code 128 for shipping/inventory
./barcode_generator.py "SHIP123456" code128

# Data Matrix for manufacturing
./barcode_generator.py "PART-ABC-001" datamatrix -o part_label

# PDF417 for documents with options
./barcode_generator.py "Document Data Here" pdf417 --options "columns=3,rows=10"

# Aztec code for transportation
./barcode_generator.py "TICKET-789" azteccode

# Show help
./barcode_generator.py --help
```

**QR Options:**
- `-o, --output`: Output filename (default: qr_code)
- `-f, --format`: Output format - png or svg (default: png)
- `-e, --error-correction`: Error correction level - L(~7%), M(~15%), Q(~25%), H(~30%) (default: M)
- `--box-size`: Size of each box in pixels (default: 10)
- `--border`: Border size in boxes (default: 4)
- `--fill-color`: Foreground color (default: black)
- `--back-color`: Background color (default: white)

**Multi-Format Options:**
- `-o, --output`: Output filename (default: barcode)
- `--options`: Barcode-specific options (format: key=value,key2=value2)
- `--list-types`: Show all available barcode types

## Examples

### EAN-13 Examples

```bash
# Generate SVG barcode for a product
./ean13_generator.py 012345678901

# Generate PNG barcode for printing
./ean13_generator.py 987654321098 -f png -o product_barcode
```

### QR Code Examples

```bash
# Website QR code
./qr_generator.py "https://github.com" -o github_qr

# Contact information
./qr_generator.py "BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1234567890
EMAIL:john@example.com
END:VCARD" -o contact_qr

# WiFi connection (replace with your network details)
./qr_generator.py "WIFI:T:WPA;S:NetworkName;P:Password;;" -o wifi_qr

# Large, high-quality QR code
./qr_generator.py "Important Document Link" -f svg -e H --box-size 20 --border 6
```

## Output Formats

### SVG
- Vector format that scales without quality loss
- Smaller file sizes for simple designs
- Ideal for web use and print
- Recommended for most use cases

### PNG
- Raster format with fixed resolution
- Widely supported by all applications
- Good for embedding in documents
- Required for some legacy systems

## Error Correction Levels (QR Codes Only)

- **L (Low)**: ~7% error correction - smallest QR codes
- **M (Medium)**: ~15% error correction - good balance (default)
- **Q (Quartile)**: ~25% error correction - good for damaged surfaces
- **H (High)**: ~30% error correction - maximum reliability

Higher error correction levels create larger QR codes but can be read even if partially damaged.

## Color Options (QR Codes Only)

Supported colors include:
- Named colors: black, white, red, green, blue, yellow, cyan, magenta, orange, purple, brown, pink, gray
- Hex colors: #000000, #FF0000, #00FF00, etc.

## Requirements

- Python 3.9+
- Ghostscript (for multi-format barcode generation)
- python-barcode[images] >= 0.15.1
- qrcode[pil] >= 7.4.2
- treepoem >= 3.25.0
- Pillow >= 8.0.0

## Supported Barcode Types

### Linear (1D) Barcodes
- **Code 128** - High-density, alphanumeric (shipping, inventory)
- **Code 39** - Alphanumeric (automotive, defense)
- **Code 93** - Compact alphanumeric
- **Interleaved 2 of 5** - Numeric only (warehouse)
- **UPC-A** - 12-digit retail
- **EAN-13** - 13-digit retail

### 2D Matrix Codes
- **QR Code** - General purpose, high compatibility
- **Data Matrix** - Small size, high density (manufacturing)
- **PDF417** - High capacity (documents, IDs)
- **Aztec Code** - Public domain (transportation)
- **MaxiCode** - Fixed size (UPS shipping)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve these tools.