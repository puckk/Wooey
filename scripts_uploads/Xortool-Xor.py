import argparse
import subprocess
import sys
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Xor Calculator', add_help=False)

parser.add_argument("-s", nargs="+", action='append', type=str, help="string with \\xAF escapes")
parser.add_argument("-h", nargs="+", action='append', type=str, help="hex-encoded string (non-letterdigit chars are stripped)")
parser.add_argument("-r", nargs="+", action='append', type=str, help="raw string")
parser.add_argument('-f', nargs='+', action='append', type=argparse.FileType('r'), help='read data from file')

def main():
    p = subprocess.check_output(["xortool-xor"]+sys.argv[1:])
    print("BIN:\n",p[:-1])
    print("HEX:\n",p.hex()[:-2])
    try:
        print("STR:\n", p.decode("utf8"))
    except:
        pass

    a = open("resultado","wb")
    a.write(p[:-1])
    a.close()
    return 0




if __name__ == "__main__":
    sys.exit(main())
