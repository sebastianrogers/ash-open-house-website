#!/usr/bin/env python3
"""
QR Code Generator for Ash Open House Website
This script generates a QR code that links to the website.
"""

import qrcode

# Website URL
WEBSITE_URL = "https://ashopenhouse.uk/"

# Output file path
OUTPUT_FILE = "website-qr-code.png"

def generate_qr_code():
    """Generate a QR code for the website URL."""
    # Create QR code instance with optimal settings
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(WEBSITE_URL)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(OUTPUT_FILE)
    print(f"QR code generated successfully: {OUTPUT_FILE}")
    print(f"URL encoded: {WEBSITE_URL}")

if __name__ == "__main__":
    generate_qr_code()
