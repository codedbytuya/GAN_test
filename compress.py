import os
import pybpg
from PIL import Image

def compress_image_with_bpg(input_file, output_file, quality=23):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        pybpg.compress(input_file, output_file, qp=quality)
        print(f"BPG: Image '{input_file}' compressed successfully as '{output_file}'.")
    except Exception as e:
        print(f"BPG: Image compression failed - {e}.")

def compress_image_with_webp(input_file, output_file, quality=85):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        img = Image.open(input_file)
        img.save(output_file, optimize=True, quality=quality, format="webp")
        print(f"WebP: Image '{input_file}' compressed successfully as '{output_file}'.")
    except Exception as e:
        print(f"WebP: Image compression failed - {e}.")

def compress_image_with_jpg(input_file, output_file, quality=85):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    try:
        img = Image.open(input_file)
        img.save(output_file, optimize=True, quality=quality)
        print(f"JPG: Image '{input_file}' compressed successfully as '{output_file}'.")
    except Exception as e:
        print(f"JPG: Image compression failed - {e}.")

# Example usage
if __name__ == "__main__":
    input_image_file = "input.png"  # Replace with your input image file path
    base_output_file = "output"     # Replace with the desired output file name (without extension)

    # Compression quality for each format (1 to 51 for BPG, 0 to 100 for WebP and JPG)
    compression_quality = 23

    # Compress in BPG format
    output_bpg_file = f"{base_output_file}.bpg"
    compress_image_with_bpg(input_image_file, output_bpg_file, compression_quality)

    # Compress in WebP format
    output_webp_file = f"{base_output_file}.webp"
    compress_image_with_webp(input_image_file, output_webp_file, compression_quality)

    # Compress in JPG format
    output_jpg_file = f"{base_output_file}.jpg"
    compress_image_with_jpg(input_image_file, output_jpg_file, compression_quality)
