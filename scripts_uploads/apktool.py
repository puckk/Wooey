import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
  description='A tool for reverse engineering 3rd party, closed, binary Android apps. It can decode resources to '
              'nearly original form and rebuild them after making some modifications. It also makes working with an '
              'app easier because of the project like file structure and automation of some repetitive tasks like '
              'building apk, etc.')

parser.add_argument('file', type=argparse.FileType('r'), help='Filename')

def main():
    a = parser.parse_args()
    options = a.file[0].name
    p = subprocess.call(["apktool"]+["d"]+[options])
    return 0




if __name__ == "__main__":
    sys.exit(main())
