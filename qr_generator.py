#!/usr/bin/env python3
"""
QR Code Generator CLI Tool
Generates QR codes in PNG or SVG format with customizable options.
"""

import argparse
import sys
import os
from pathlib import Path

try:
    import qrcode
    from qrcode.constants import (
        ERROR_CORRECT_L, ERROR_CORRECT_M, 
        ERROR_CORRECT_Q, ERROR_CORRECT_H
    )
    from PIL import Image
except ImportError:
    print("Error: qrcode library not found.")
    print("Please install it with: pip install 'qrcode[pil]'")
    sys.exit(1)


def get_error_correction_level(level):
    """Map error correction level string to qrcode constant."""
    levels = {
        'L': ERROR_CORRECT_L,  # ~7% error correction
        'M': ERROR_CORRECT_M,  # ~15% error correction
        'Q': ERROR_CORRECT_Q,  # ~25% error correction
        'H': ERROR_CORRECT_H   # ~30% error correction
    }
    return levels.get(level.upper(), ERROR_CORRECT_M)


def generate_qr_code(data, output_path, format_type='png', box_size=10, border=4, 
                     error_correction='M', fill_color='black', back_color='white'):
    """Generate QR code and save to file."""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=get_error_correction_level(error_correction),
            box_size=box_size,
            border=border,
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        if format_type.lower() == 'svg':
            from qrcode.image.svg import SvgPathImage
            img = qr.make_image(image_factory=SvgPathImage, 
                               fill_color=fill_color, 
                               back_color=back_color)
            file_extension = '.svg'
        else:
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            file_extension = '.png'
        
        # Add extension if not provided
        output_path = str(Path(output_path))
        if not output_path.endswith(file_extension):
            output_path += file_extension
        
        img.save(output_path)
        return output_path
        
    except Exception as e:
        raise Exception(f"Failed to generate QR code: {e}")


def validate_colors(fill_color, back_color):
    """Validate color inputs."""
    valid_colors = {
        'black', 'white', 'red', 'green', 'blue', 'yellow', 
        'cyan', 'magenta', 'orange', 'purple', 'brown', 'pink', 'gray'
    }
    
    # Allow hex colors (starting with #)
    if fill_color.startswith('#') or fill_color.lower() in valid_colors:
        pass
    else:
        raise ValueError(f"Invalid fill color: {fill_color}")
    
    if back_color.startswith('#') or back_color.lower() in valid_colors:
        pass
    else:
        raise ValueError(f"Invalid background color: {back_color}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes with customizable options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Hello World"
  %(prog)s "https://example.com" -o website_qr
  %(prog)s "Contact info" -f svg -e H --box-size 15
  %(prog)s "Data" --fill-color red --back-color yellow
        """
    )
    
    parser.add_argument(
        'data',
        help='Data to encode in the QR code'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='qr_code',
        help='Output filename (default: qr_code)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['png', 'svg'],
        default='png',
        help='Output format (default: png)'
    )
    
    parser.add_argument(
        '-e', '--error-correction',
        choices=['L', 'M', 'Q', 'H'],
        default='M',
        help='Error correction level: L(~7%%), M(~15%%), Q(~25%%), H(~30%%) (default: M)'
    )
    
    parser.add_argument(
        '--box-size',
        type=int,
        default=10,
        help='Size of each box in pixels (default: 10)'
    )
    
    parser.add_argument(
        '--border',
        type=int,
        default=4,
        help='Border size in boxes (default: 4)'
    )
    
    parser.add_argument(
        '--fill-color',
        default='black',
        help='Foreground color (default: black)'
    )
    
    parser.add_argument(
        '--back-color',
        default='white',
        help='Background color (default: white)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='QR Code Generator 1.0.0'
    )
    
    args = parser.parse_args()
    
    try:
        validate_colors(args.fill_color, args.back_color)
        
        filename = generate_qr_code(
            args.data,
            args.output,
            args.format,
            args.box_size,
            args.border,
            args.error_correction,
            args.fill_color,
            args.back_color
        )
        
        print(f"QR code generated successfully: {filename}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()