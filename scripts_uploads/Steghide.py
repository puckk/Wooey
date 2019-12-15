import argparse
import sys
import subprocess
import os

#dependencia:
#apt-get install steghide

parser = argparse.ArgumentParser(description="Steghide is a steganography program that is able to hide data in "
                                             "various kinds of image- and audio-files. The color- respectivly "
                                             "sample-frequencies are not changed thus making the embedding resistant "
                                             "against first-order statistical tests.")


subparsers = parser.add_subparsers()

parser_1 = subparsers.add_parser("extract", help="Extract Method")
parser_1.add_argument('-sf', type=argparse.FileType("r"), help='Stego File. Archivo stego')
parser_1.add_argument('-p', help='Password', default="")


parser_2 = subparsers.add_parser("embed", help="Embed Method")
parser_2.add_argument('-cf', '--coverfile', type=argparse.FileType("r"), help='Elegir archivo de portada')
parser_2.add_argument('-ef', '--embedfile', type=argparse.FileType("r"), help='Elegir archivo para adjuntar')
parser_2.add_argument('-p', help='Password', default="")
#

def main():
    if not "-p" in sys.argv:
        c = ["steghide"] + sys.argv[1:] + ["-p"] + [""]
    else:
        c = ["steghide"] + sys.argv[1:]
    subprocess.call(c)
    return 0




if __name__ == "__main__":
    sys.exit(main())