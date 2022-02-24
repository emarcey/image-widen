import argparse
import os
from PIL import Image


SOURCE_DIR = f"{os.getcwd()}/originals"
OUTPUT_DIR = f"{os.getcwd()}/modified"

parser = argparse.ArgumentParser(description="help")
parser.add_argument("--original_file", type=str, help="name of the original file to use")
parser.add_argument("--source_dir", type=str, help="name of the source directory", default=SOURCE_DIR)
parser.add_argument("--output_dir", type=str, help="name of the output directory", default=OUTPUT_DIR)


def main(original_file: str, source_dir: str, output_dir: str) -> None:
    original = Image.open(f"{source_dir.rstrip('/')}/{original_file}")
    if original.height != original.width:
        raise ValueError("Program only handles square files")

    background = Image.new("RGB", (original.width * 2, original.height), "white")
    background.paste(original, (original.width // 2, 0))
    full_filename = original_file.split("/")[-1].split(".")
    filename = full_filename[0]
    extension = ".".join(full_filename[1:])
    background.save(f"{output_dir.rstrip('/')}/{filename}_modified.{extension}")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.original_file, args.source_dir, args.output_dir)
