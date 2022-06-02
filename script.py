import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="path to create file structure")
args = parser.parse_args()

current_dir = os.getcwd()

# Creating File Structure for flask apps


def create_file_structure(path=current_dir):
    """
    Creates Flask file structure in the current directory
    """
    # creating dirs at root first
    dir_list = ['static/css', "static/js", 'templates']
    for files in dir_list:
        os.makedirs(files)
    # creating files
    file_list = ["app.py", "static/css/style.css", "static/js/app.js",
                 "templates/index.html", "templates/contact.html", "templates/about.html"]
    for file in file_list:
        with open(file, "w") as f:
            f.close()


if __name__ == "__main__":
    if args.filepath:
        try:
            if os.path.isdir(args.filepath):
                print(f"[+] creating file structure in {args.filepath}")
                create_file_structure(path=args.filepath)
                print("[*] file structure created.")
        except Exception:
            print("[!] invalid file path.")
    else:
        print("[+] creating file structure in current directory.")
        create_file_structure()
        print("[*] file structure created.")
