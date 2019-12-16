import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(
  description='DIRB is a command line based tool to brute force any directory based on wordlists. DIRB will make an '
              'HTTP request and see the HTTP response code of each request')

parser.add_argument('url', type=str, help='Base URL to scan.', nargs='+')
parser.add_argument('wordlist', nargs='?', choices=["/wordlists/rockyou.txt"], help="Output_file")


parser.add_argument('-E', type=argparse.FileType('r'), help='Client Certificate')

parser.add_argument("-a", type=str, help="Custom User Agent")
parser.add_argument("-c", type=str, help="Set a cookie for the HTTP request")
parser.add_argument("-H", type=str, help="Add a custom header to the HTTP request")
parser.add_argument("-o", type=str, help="Save output to disk")
parser.add_argument("-u", type=str, help="HTTP Authentication. <username:password>")
parser.add_argument("-X", type=str, help="Append each word with this extensions")
parser.add_argument("-N", type=int, help="Ignore responses with this HTTP code")
parser.add_argument("-z", type=int, help="Add a milliseconds delay to not cause excessive Flood")
parser.add_argument("-b", action="store_true", help="Use path as is")
parser.add_argument("-f", action="store_true", help="Fine tunning of NOT_FOUND (404) detection")
parser.add_argument("-w", action="store_true", help="Don't stop on WARNING messages.")
parser.add_argument("-i", action="store_true", help="Use case-insensitive search")
parser.add_argument("-l", action="store_true", help='Print "Location" header when found')
parser.add_argument("-r", action="store_true", help="Don't search recursively.")
parser.add_argument("-S", action="store_true", help="Silent Mode. Don't show tested words.")
parser.add_argument("-t", action="store_true", help="Don't force an ending '/' on URLs.")
parser.add_argument("-v", action="store_true", help="Show also NOT_FOUND pages.")


def main():
    a = parser.parse_args()
    p = subprocess.call(["dirb"]+sys.argv[1:])
    return 0




if __name__ == "__main__":
    sys.exit(main())
