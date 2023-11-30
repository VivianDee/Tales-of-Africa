import sys
from PIL import Image
import os

def create_thumbnail(image_path):
    # Open the original image using Pillow
    with Image.open(image_path) as img:
        # Create the path for the thumbnail with a WebP extension
        thumbnail_path = f"thumb_{os.path.basename(image_path).split('.')[0]}.webp"

        # Convert and save the image as WebP with a reasonable quality setting
        img.save(thumbnail_path, format='WebP', quality=80)  # Adjust quality as needed

    return thumbnail_path

if __name__ == "__main__":
    # Check if an image file name is provided in the command line arguments
    if len(sys.argv) != 2:
        print("Usage: python create_thumbnail.py <image_file_name>")
        sys.exit(1)

    # Get the image file name from the command line
    image_file_name = sys.argv[1]

    # Create a thumbnail
    thumbnail_path = create_thumbnail(image_file_name)

    print(f"Thumbnail created at: {thumbnail_path}")
