#!/usr/bin/env python3
"""
Multi-Format Barcode Generator CLI Tool
Generates various barcode types including Code 128, Data Matrix, PDF417, and more.
"""

import argparse
import sys
import os
from pathlib import Path

try:
    import treepoem
    from PIL import Image, ImageOps
except ImportError:
    print("Error: Required libraries not found.")
    print("Please install with: pip install treepoem Pillow")
    print("Note: You also need Ghostscript installed on your system")
    sys.exit(1)


# Supported barcode types with descriptions
BARCODE_TYPES = {
    'code128': 'Code 128 - High-density linear barcode for alphanumeric data',
    'datamatrix': 'Data Matrix - 2D matrix code for small spaces and high data density',
    'pdf417': 'PDF417 - 2D stacked barcode with high data capacity',
    'azteccode': 'Aztec Code - 2D matrix code used in transportation',
    'code39': 'Code 39 - Alphanumeric linear barcode',
    'code93': 'Code 93 - Compact alphanumeric linear barcode',
    'interleaved2of5': 'Interleaved 2 of 5 - Numeric-only linear barcode',
    'qrcode': 'QR Code - 2D matrix code (use qr_generator.py for more options)',
    'upca': 'UPC-A - 12-digit retail barcode',
    'ean13': 'EAN-13 - 13-digit retail barcode (use ean13_generator.py for more options)',
    'maxicode': 'MaxiCode - Fixed-size 2D code used by UPS',
    'codablock': 'Codablock F - Stacked linear barcode'
}


def validate_barcode_type(barcode_type):
    """Validate that the barcode type is supported."""
    if barcode_type not in BARCODE_TYPES:
        available = ', '.join(sorted(BARCODE_TYPES.keys()))
        raise ValueError(f"Unsupported barcode type '{barcode_type}'. Available types: {available}")
    return barcode_type


def generate_barcode(data, barcode_type, output_path, options=None):
    """Generate barcode using treepoem and save to file."""
    try:
        validated_type = validate_barcode_type(barcode_type)
        
        # Generate the barcode
        image = treepoem.generate_barcode(
            barcode_type=validated_type,
            data=data,
            options=options or {}
        )
        
        # Add white border for better readability
        image = ImageOps.expand(image, border=10, fill="white")
        
        # Determine output format based on file extension
        output_path = Path(output_path)
        if not output_path.suffix:
            output_path = output_path.with_suffix('.png')
        
        # Convert and save
        if output_path.suffix.lower() == '.png':
            # Convert to RGB for PNG (treepoem returns 1-bit images)
            image = image.convert('RGB')
        
        image.save(str(output_path))
        return str(output_path)
        
    except ValueError as e:
        raise ValueError(str(e))
    except Exception as e:
        raise Exception(f"Failed to generate barcode: {e}")


def parse_options(options_str):
    """Parse options string into dictionary."""
    if not options_str:
        return {}
    
    options = {}
    try:
        for pair in options_str.split(','):
            if '=' in pair:
                key, value = pair.strip().split('=', 1)
                options[key.strip()] = value.strip()
            else:
                # Boolean option
                options[pair.strip()] = True
        return options
    except Exception as e:
        raise ValueError(f"Invalid options format: {e}")


def list_barcode_types():
    """Print all available barcode types with descriptions."""
    print("Available barcode types:")
    print("=" * 50)
    for code, description in sorted(BARCODE_TYPES.items()):
        print(f"{code:15} - {description}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate various types of barcodes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "ABC123" code128
  %(prog)s "https://example.com" datamatrix -o website_dm
  %(prog)s "Document ID: 12345" pdf417 --options "columns=3,rows=10"
  %(prog)s --list-types

Barcode Types:
  code128      - Code 128 (shipping, inventory)
  datamatrix   - Data Matrix (manufacturing, small items)
  pdf417       - PDF417 (documents, IDs)
  azteccode    - Aztec Code (transportation)
  code39       - Code 39 (automotive, defense)
        """
    )
    
    parser.add_argument(
        'data',
        nargs='?',
        help='Data to encode in the barcode'
    )
    
    parser.add_argument(
        'type',
        nargs='?',
        help='Barcode type (see --list-types for all options)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='barcode',
        help='Output filename (default: barcode)'
    )
    
    parser.add_argument(
        '--options',
        help='Barcode-specific options (format: key=value,key2=value2)'
    )
    
    parser.add_argument(
        '--list-types',
        action='store_true',
        help='List all available barcode types'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='Multi-Format Barcode Generator 1.0.0'
    )
    
    args = parser.parse_args()
    
    if args.list_types:
        list_barcode_types()
        return
    
    if not args.data or not args.type:
        parser.error("Both 'data' and 'type' are required (unless using --list-types)")
    
    try:
        options = parse_options(args.options)
        
        filename = generate_barcode(
            args.data,
            args.type,
            args.output,
            options
        )
        
        print(f"Barcode generated successfully: {filename}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()