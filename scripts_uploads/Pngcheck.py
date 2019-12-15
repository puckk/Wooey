import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
  description='pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the internal 32-bit CRCs ['
              'checksums] and decompressing the image data); it can optionally dump almost all of the chunk-level '
              'information in the image in human-readable form. For example, it can be used to print the basic '
              'statistics about an image (dimensions, bit depth, etc.); to list the color and transparency info in '
              'its palette (assuming it has one); or to extract the embedded text annotations. This is a command-line '
              'program with batch capabilities.')

parser.add_argument('img', type=argparse.FileType('r'), help='Filename', nargs='+')
parser.add_argument("-7", action="store_true", help="Print contents of tEXt chunks, escape chars >=128 (for 7-bit terminals)")
parser.add_argument("-f", action="store_true", help="Force continuation even after major errors")
parser.add_argument("-p", action="store_true", help="Print contents of PLTE, tRNS, hIST, sPLT and PPLT")
parser.add_argument("-q", action="store_true", help="Test quietly (output only errors)")
parser.add_argument("-s", action="store_true", help="Search for PNGs within another file")
parser.add_argument("-t", action="store_true", help="Print contents of tEXt chunks")
parser.add_argument("-v", action="store_true", help="Test verbosely (print most chunk data)")
parser.add_argument("-x", action="store_true", help="Search for PNGs within another file and extract them when found")


def main():
    a = parser.parse_args()
    filename = a.img[0].name
    options = sys.argv[1:]
    options.remove(a.img[0].name)
    command = ["pngcheck"]+options+[filename]
    p = subprocess.call(["pngcheck"]+options+[filename])
    return 0




if __name__ == "__main__":
    sys.exit(main())
