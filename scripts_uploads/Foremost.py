import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
  description='Foremost is a Linux program to recover files based on their headers and footers. Foremost can work on '
              'image files, such as those generated by dd, Safeback, Encase, etc, or directly on a drive. The headers '
              'and footers are specified by a configuration file, so you can pick and choose which headers you want '
              'to look for.')

parser.add_argument('file', type=argparse.FileType('r'), help='Filename')

def main():
    a = parser.parse_args()
    p = subprocess.call(["foremost"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
