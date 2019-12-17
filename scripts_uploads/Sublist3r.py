import argparse
import sys
import subprocess
import os

#dependencia:
#cd /usr/share
#git clone https://github.com/aboul3la/Sublist3r.git
#cd Sublist3r
#sudo pip install -r requirements.txt
#echo -e '#!/bin/bash\ncd /usr/share/Sublist3r && ./sublist3r.py "$@"' > /usr/bin/sublist3r

parser = argparse.ArgumentParser(description="Enumerate subdomains of websites using OSINT.")


parser.add_argument('-d', type=str, help='Domain name to enumerate subdomains of (ex: google.com)', required=True)
parser.add_argument("-b", "--bruteforce",help='Enable the subbrute bruteforce module', action="store_true")
parser.add_argument('-p', "--ports", type=str, help='Scan the found subdomains against specific tcp ports (ex: 80,443)')
parser.add_argument("-v", "--verbose",help='Enable berbose', action="store_true")


def main():

    subprocess.call(["sublist3r"]+ sys.argv[1:])

    return 0



if __name__ == "__main__":
    sys.exit(main())
