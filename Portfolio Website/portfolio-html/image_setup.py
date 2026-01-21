#!/usr/bin/env python3
"""
Image Setup Helper - Converts images to base64 and embeds in HTML
Run this script after placing your images in the images/ folder
"""

import os
import base64
from pathlib import Path

def image_to_base64(image_path):
    """Convert image file to base64 string"""
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_image_mime_type(image_path):
    """Get MIME type based on file extension"""
    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    return mime_types.get(ext, 'image/jpeg')

def main():
    images_dir = Path(__file__).parent / 'images'
    
    print("=" * 60)
    print("📸 Image Setup Helper")
    print("=" * 60)
    
    # Check if images folder exists
    if not images_dir.exists():
        print(f"❌ Images folder not found at: {images_dir}")
        print(f"📁 Please create: {images_dir}")
        return
    
    # Look for images
    image_files = list(images_dir.glob('*.*'))
    image_files = [f for f in image_files if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']]
    
    if not image_files:
        print(f"❌ No images found in: {images_dir}")
        print("📝 Instructions:")
        print("1. Save your first 2 profile images to the images folder")
        print("2. Name them as: profile1.jpg and profile2.jpg (or any image names)")
        print("3. Run this script again")
        return
    
    print(f"✅ Found {len(image_files)} image(s)")
    
    # Show found images
    for i, img_file in enumerate(image_files, 1):
        file_size = img_file.stat().st_size / 1024  # KB
        print(f"   {i}. {img_file.name} ({file_size:.1f} KB)")
    
    print("\n✨ To use these images:")
    print("   1. Rename your images to: profile.jpg (for hero & about sections)")
    print("   2. Or contact support to embed them directly")
    print("\n📍 Images should be saved at:")
    print(f"   {images_dir}/")

if __name__ == "__main__":
    main()
