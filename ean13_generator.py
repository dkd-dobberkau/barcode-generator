#!/usr/bin/env python3
"""
EAN-13 Barcode Generator CLI Tool
Generates EAN-13 barcodes in SVG or PNG format.
"""

import argparse
import sys
import os
from pathlib import Path

try:
    import barcode
    from barcode import EAN13
    from barcode.writer import ImageWriter, SVGWriter
except ImportError:
    print("Error: python-barcode library not found.")
    print("Please install it with: pip install 'python-barcode[images]'")
    sys.exit(1)


def validate_ean13_code(code):
    """Validate EAN-13 code format (12 digits)."""
    if not code.isdigit():
        raise ValueError("EAN-13 code must contain only digits")
    
    if len(code) != 12:
        raise ValueError("EAN-13 code must be exactly 12 digits")
    
    return code


def generate_barcode(code, output_path, format_type='svg'):
    """Generate EAN-13 barcode and save to file."""
    try:
        validated_code = validate_ean13_code(code)
        
        if format_type.lower() == 'png':
            writer = ImageWriter()
            file_extension = '.png'
        else:
            writer = SVGWriter()
            file_extension = '.svg'
        
        ean = EAN13(validated_code, writer=writer)
        
        # Remove extension from output_path if provided
        output_path = str(Path(output_path).with_suffix(''))
        
        # Save the barcode
        filename = ean.save(output_path)
        
        return filename
        
    except ValueError as e:
        raise ValueError(f"Invalid EAN-13 code: {e}")
    except Exception as e:
        raise Exception(f"Failed to generate barcode: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate EAN-13 barcodes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 123456789012
  %(prog)s 123456789012 -o my_barcode
  %(prog)s 123456789012 -f png -o barcode.png
        """
    )
    
    parser.add_argument(
        'code',
        help='12-digit EAN-13 code (checksum will be calculated automatically)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='barcode',
        help='Output filename (default: barcode)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['svg', 'png'],
        default='svg',
        help='Output format (default: svg)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='EAN-13 Generator 1.0.0'
    )
    
    args = parser.parse_args()
    
    try:
        filename = generate_barcode(args.code, args.output, args.format)
        print(f"Barcode generated successfully: {filename}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()