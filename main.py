import argparse
import pathlib
import os

ap = argparse.ArgumentParser()

ap.add_argument("-f", "--folder", required=True, help="What folder the code is in")
ap.add_argument('-e', '--endswith', required=False, help='What the file you want to check ends with.')

args = vars(ap.parse_args())

folder_full_path = os.path.abspath(args["folder"])
fileending = args['endswith']
if fileending != None:
    print(f"I'm looking for files ending with " + fileending)

total_lines = 0

if pathlib.Path(folder_full_path).is_dir():
    print(f'Folders full path is: {folder_full_path}')
    for path in pathlib.Path(folder_full_path).iterdir():
        if path.is_file():
            path = str(path)
            if fileending == None:
                current_file = open(path, "r")
                lines = current_file.readlines()
                nummber_of_lines = len(lines)
                total_lines += nummber_of_lines
            elif path.endswith(fileending):
                current_file = open(path, "r")
                lines = current_file.readlines()
                nummber_of_lines = len(lines)
                total_lines += nummber_of_lines

    print(f" Total lines: {total_lines}")
else:
    print("Not a directory")
