import argparse
import sys
import subprocess
import os

parser = argparse.ArgumentParser(description="Commix - Automated All-in-One OS Command Injection and Exploitation Toolr.")

parser.add_argument('-u', help='Target URL.', type=str,required=True)
parser.add_argument('-v',help="Verbosity level.",choices=('0','1','2','3','4'), type=str)

#request
req = parser.add_argument_group("Request")
req.add_argument('--host',help='HTTP host header.', type=str)
req.add_argument('--referer',help='HTTP referer header.', type=str)
req.add_argument('--user-agent',help='HTTP User-Agent header.', type=str)
req.add_argument('--random-agent',help='Use random User-Agent header.', action="store_true")
req.add_argument('--cookie',help='HTTP cookie header.', type=str)
req.add_argument('-H',help="Extra header (e.g. 'X-Forwarded-For: 127.0.0.1').", type=str)
req.add_argument('--headers',help="Extra headers (e.g. 'Accept-Language: fr\nETag: 123').", type=str)

#enumeration
enum = parser.add_argument_group("Enumeration")
enum.add_argument('--all',help='Retrieve everything.', action="store_true")
enum.add_argument('--current-user',help='Retrieve current username.', action="store_true")
enum.add_argument('--hostname',help='Retrieve current hostname.', action="store_true")
enum.add_argument('--sys-info',help='Retrieve system information.', action="store_true")
enum.add_argument('--users',help='Retrieve system users.', action="store_true")
enum.add_argument('--passwords',help='Retrieve system users password hashes.', action="store_true")

#file access
fa = parser.add_argument_group("File Access")
fa.add_argument('--file-read',help="Read a file from the target host.", type=str)
fa.add_argument('--file-write',help="Write to a file on the target host.", type=str)

#injection
inj = parser.add_argument_group("Injection")
inj.add_argument('-d','--data',help='Data string to be sent through POST.', type=str)
inj.add_argument('-p',help="Testable parameter(s)", type=str)
inj.add_argument('--skip',help="Skip testing for given parameter(s).", type=str)
inj.add_argument('--suffix',help="Injection payload suffix string.", type=str)
inj.add_argument('--prefix',help="Injection payload prefix string.", type=str)
inj.add_argument('--technique',help="Specify injection technique(s) to use.", type=str)
inj.add_argument('--os-cmd',help="Execute a single operating system command.", type=str)
inj.add_argument('--os',choices=('Windows','Unix'),help="Back-end operating system", type=str)
#detection
det = parser.add_argument_group("Detection")
det.add_argument('--level',help="Level of tests to perform",choices=('1','2','3'), type=str)


def main():
    subprocess.call(["commix"] + sys.argv[1:])
    return 0

if __name__ == "__main__":
    sys.exit(main())
