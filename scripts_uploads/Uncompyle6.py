import argparse
import subprocess
import sys
import os

parser = argparse.ArgumentParser(
  description='Python cross-version byte-code decompiler.')

parser.add_argument('file', type=argparse.FileType('r'), help='Filename', nargs='+')
parser.add_argument('-p', type=int, help='Number of processes')
parser.add_argument('--verify', action="store_true", help='Compare generated source with input byte-code')



def main():
    a = parser.parse_args()
    fi = os.path.basename(a.file[0].name)[:-1]
    command = ["uncompyle6"]+["-o"]+[fi]+sys.argv[1:]
    print(command)
    p = subprocess.call(command)
    return 0


if __name__ == "__main__":
    sys.exit(main())
