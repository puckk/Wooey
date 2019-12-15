import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
    description='Universal Steganographic Tool')

parser.add_argument('-k', type=str, help='Specify the secret key used to encrypt and hide the message in the provided '
                                         'data.')
parser.add_argument('-d', type=argparse.FileType('r'), help='Specify the filename containing a message to be hidden '
                                                            'in the data')
parser.add_argument('-s', type=str, help='Specify the initial seed the iterator object uses for selecting bits in the '
                                         'redundant data. If no upper limit is specified, the iterator will use this '
                                         'seed without searching for a more optimal embedding.')

parser.add_argument('-i', '--limit', type=int, help='Specify the upper limit for finding an optimal iterator seed. '
                                                    'The maximum value for the limit is 65535.')
parser.add_argument('-e', '--prime', action="store_true", help='Use error correction for data encoding and decoding.')
parser.add_argument('-r', type=argparse.FileType('r'), help='Retrieve a message from a data object. If this option is '
                                                            'not specified, outguess will embed messages.')
parser.add_argument('-x', type=int, help='If the second key does not create an iterator object that is successful in '
                                         'embedding the data, the program will derive up to specified number of new '
                                         'keys.')
parser.add_argument('-p', type=str, help='Passes a string as parameter to the destination data handler. For the JPEG '
                                         'image format, this is the compression quality, it can take values between '
                                         '75 and 100. The higher the quality the more bits to hide a message in the '
                                         'data are available.')
parser.add_argument('-m', action="store_true", help='Mark pixels that have been modified.')
parser.add_argument('-t', action="store_true", help='Collect statistics about redundant bit usage. Repeated use '
                                                    'increases output level.')
parser.add_argument('input', nargs='?', type=argparse.FileType('r'), help='Filename')
parser.add_argument('output', nargs='?', type=str, help="Output_file")

def main():
    a = parser.parse_args()
    p = subprocess.call(["outguess"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
