import argparse
import sys
import subprocess
import os

#dependencia:
#pip install wfuzz

parser = argparse.ArgumentParser(description="The web fuzzer.")


parser.add_argument('-w', help='The dictionary file', type=argparse.FileType('r'), required=True)
parser.add_argument('host', type=str, help='Website to scan. Must indicate the fuzzing point (ex: http://google.com/FUZZ)')
parser.add_argument('-s', type=int, default=0, help='Specify time delay between requests in seconds (0 default)')
parser.add_argument('-X', type=str, help='Specify an HTTP method for the request')
parser.add_argument('-b', type=str, help='Specify a cookie for the requests')
parser.add_argument('-d', type=str, help='Use post data (ex: "id=FUZZ&catalogue=1")')

parser.add_argument('-v', help='Verbose information', action='store_true')
#parser.add_argument('-c', help='Color?', action='store_true')

def main():

    subprocess.call(["wfuzz"] + sys.argv[1:])

    return 0



if __name__ == "__main__":
    sys.exit(main())
