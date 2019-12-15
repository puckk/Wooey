import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
  description='Binwalk is a fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images.')

parser.add_argument('file', type=argparse.FileType('r'), help='Filename', nargs='+')
eo = parser.add_argument_group("Extract options")
eo.add_argument("-e", "--extract", action="store_true", help="Automatically extract known file types")
eo.add_argument("-D", "--dd", type=str, help="Extract type signatures, give the files an extension of ext, "
                                               "and execute cmd")
en = parser.add_argument_group("Entropy Analysis")
en.add_argument("-E", "--entropy", action="store_true", help="Calculate file entropy")
en.add_argument("-F", "--fast", action="store_true", help="Use faster, but less detailed, entropy analysis")
en.add_argument("-J", "--save", action="store_true", help="Save plot as a PNG")



def main():
    a = parser.parse_args()
    p = subprocess.call(["binwalk"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
