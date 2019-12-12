import argparse
import sys
import subprocess
import os

#dependencia:
#apt-get install sqlmap

parser = argparse.ArgumentParser(description="Sqlmap script. (BATCH MODE)")
parser.add_argument('-u', type=str, help='Url to scan', required=True)

#request
parser.add_argument('--data', type=str, help='Data string to be sent through POST')
parser.add_argument('--cookie', type=str, help='HTTP Cookie header value')


#injection
parser.add_argument('-p', type=str, help='Testable parameter(s)')

#detection
parser.add_argument('--level', type=int, default=1, choices=range(1, 6), help='Level of tests to perform (1-5, default 1)')
parser.add_argument('--risk', type=int, default=1, choices=range(1, 4), help='Risk of tests to perform (1-3, default 1)')

#options
parser.add_argument('-v', type=int, default=1, choices=range(0, 7), help='Verbosity level: 0-6 (default 1)')

#parser.add_argument('--batch', help='Do not require input.', action='store_true')

def main():

    #le agregue para que corra en batch porque creo q wooey no es interactivo
    subprocess.call(["sqlmap"] + sys.argv[1:] + ["--batch"])
    return 0



if __name__ == "__main__":
    sys.exit(main())
