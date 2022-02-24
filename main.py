import argparse
from datetime import datetime
import os
from PIL import Image
import requests
from typing import Optional, Tuple


SOURCE_DIR = f"{os.getcwd()}/originals"
OUTPUT_DIR = f"{os.getcwd()}/modified"

parser = argparse.ArgumentParser(description="help")
parser.add_argument("--original_file", type=str, help="name of the original file to use", default=None)
parser.add_argument("--original_url", type=str, help="url for the original file to use", default=None)
parser.add_argument("--source_dir", type=str, help="name of the source directory", default=SOURCE_DIR)
parser.add_argument("--output_dir", type=str, help="name of the output directory", default=OUTPUT_DIR)


def transform_and_save(original: Image.Image, output_dir: str, filename: str, file_extension: str) -> None:
    background = Image.new("RGB", (original.width * 2, original.height), "white")
    background.paste(original, (original.width // 2, 0))
    background.save(f"{output_dir.rstrip('/')}/{filename}_modified.{file_extension}")


def from_image(original_file: str, source_dir: str) -> Tuple[Image.Image, str, str]:
    original = Image.open(f"{source_dir.rstrip('/')}/{original_file}")
    if original.height != original.width:
        raise ValueError("Program only handles square files")
    full_filename = original_file.split("/")[-1].split(".")
    filename = full_filename[0]
    extension = ".".join(full_filename[1:])
    return original, filename, extension


def from_url(original_url: str) -> Tuple[Image.Image, str, str]:
    image = Image.open(requests.get(original_url, stream=True).raw)
    return image, f"url_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}", "jpg"


if __name__ == "__main__":
    args = parser.parse_args()
    original_image: Optional[Image.Image] = None
    filename = ""
    file_extension = ""
    if args.original_file:
        original_image, filename, file_extension = from_image(args.original_file, args.source_dir)
    elif args.original_url:
        original_image, filename, file_extension = from_url(args.original_url)
    else:
        raise ValueError("Need either original file or url")

    if not original_image:
        raise ValueError("No image created")

    transform_and_save(original_image, args.output_dir, filename, file_extension)
