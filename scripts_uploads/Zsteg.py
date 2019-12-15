import argparse
import subprocess
import sys
import tempfile
# dependencia:
# apt-get install sqlmap

parser = argparse.ArgumentParser(
    description='Detect stegano-hidden data in PNG & BMP. LSB steganography in PNG & BMP. zlib-compressed data. '
                'OpenStego. Camouflage 1.2.1. LSB with The Eratosthenes set')

parser.add_argument('filename', type=argparse.FileType('r'), help='Filename')
parser.add_argument('-c', type=str, help='channels (R/G/B/A) or any combination, comma separated, valid values: r,g,'                                         'b,a,rg,bgr,rgba,r3g2b3,...')
parser.add_argument('-l', '--limit', type=int, help='Limit bytes checked, 0 = no limit (default: 256)')
parser.add_argument('-b', '--bits', type=str, help='number of bits, single int value or \'1,3,5\' or range \'1-8\'')

parser.add_argument('--lsb', action="store_true", help='least significant BIT comes first')
parser.add_argument('--msb', action="store_true", help='most significant BIT comes first')
parser.add_argument('-P', '--prime', action="store_true", help='most significant BIT comes first')
parser.add_argument('--invert', action="store_true", help='invert bits (XOR 0xff)')
parser.add_argument('-a', '--all', action="store_true", help='try all known methods')
parser.add_argument('-o', type=str, help='pixel iteration order (default: \'auto\')')
parser.add_argument('-E', '--extract', type=str, help='extract specified payload, NAME is like \'1b,rgb,lsb\'')
parser.add_argument('-s', '--strings', choices=["first", "all", "longest", "none"], help='extract specified payload, '
                                                                                         'NAME is like \'1b,rgb,lsb\'')
parser.add_argument('-v', action="store_true", help='Run verbosely')




def main():
    a = parser.parse_args()
    p = subprocess.call(["zsteg"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
