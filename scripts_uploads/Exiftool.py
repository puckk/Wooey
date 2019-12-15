import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
    description='ExifTool is a platform-independent Perl library plus a command-line application for reading, '
                'writing and editing meta information in a wide variety of files. ExifTool supports many different '
                'metadata formats including EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, '
                'FlashPix, AFCP and ID3, as well as the maker notes of many digital cameras by Canon, Casio, DJI, '
                'FLIR, FujiFilm, GE, GoPro, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Motorola, Nikon, '
                'Nintendo, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Phase One, Reconyx, Ricoh, Samsung, Sanyo, '
                'Sigma/Foveon and Sony.')

parser.add_argument('file', type=argparse.FileType('r'), help='Filename')


def main():
    a = parser.parse_args()
    p = subprocess.call(["exiftool"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
