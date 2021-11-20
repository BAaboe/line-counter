import argparse
import pathlib
import os

ap = argparse.ArgumentParser()

ap .add_argument("-f", "--folder", required=True, help="What folder the code is in")

args = vars(ap.parse_args())

folder_full_path = os.path.abspath(args["folder"])

total_lines = 0

if pathlib.Path(folder_full_path).is_dir():
    print(f'Folders full path is: {folder_full_path}')
    for path in pathlib.Path(folder_full_path).iterdir():
        if path.is_file():
            current_file = open(path, "r")
            lines = current_file.readlines()
            nummber_of_lines = len(lines)
            total_lines += nummber_of_lines

    print(f" Total lines: {total_lines}")

else:
    print("Not a directory")
