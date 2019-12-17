import argparse
import sys
import subprocess
import os

parser = argparse.ArgumentParser(description="Gobuster v3.0.1.")

parser.add_argument('-w', help='Path to the wordlist file', type=str)
parser.add_argument('-v', help='Verbose mode', action='store_true')

subparsers = parser.add_subparsers()

parser_dns = subparsers.add_parser('dns')
parser_dns.add_argument('-d', help='The target domain', type=str)
parser_dns.add_argument('-r', "--resolver", help='Use custom DNS server (format server.com or server.com:port)', type=str)
group = parser_dns.add_mutually_exclusive_group()
group.add_argument("-c", "--showcname",help='Show CNAME records', action="store_true")
group.add_argument("-i", "--showips", help='Show IP addresses', action="store_true")

parser_dir = subparsers.add_parser('dir')

parser_dir.add_argument('-u', "--url", help='The target url', type=str)
parser_dir.add_argument('-f', "--addslash", help='Append / to each request', action="store_true")
parser_dir.add_argument('-c', "--cookies", help='Cookies to use for the requests', type=str)
parser_dir.add_argument('-x', "--extensions", help='File extension(s) to search for', type=str)
parser_dir.add_argument('-r', "--followredirect", help='Follow redirects', action="store_true")

parser_dir.add_argument('-U', "--username", help='Username for Basic Auth', type=str)
parser_dir.add_argument('-P', "--password", help='Password for Basic Auth', type=str)

parser_vhost = subparsers.add_parser('vhost')
parser_vhost.add_argument('-d', help='The target domain', type=str)
parser_vhost.add_argument('-c', "--cookies", help='Cookies to use for the requests', type=str)
parser_vhost.add_argument('-r', "--followredirect", help='Follow redirects', action="store_true")
parser_vhost.add_argument('-U', "--username", help='Username for Basic Auth', type=str)
parser_vhost.add_argument('-P', "--password", help='Password for Basic Auth', type=str)


def main():
    subprocess.call(["gobuster"] + sys.argv[1:])
    return 0

if __name__ == "__main__":
    sys.exit(main())
