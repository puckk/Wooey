import argparse
import subprocess
import sys

# dependencia:
# apt-get install nmap

parser = argparse.ArgumentParser(
    description="Nikto is an Open Source (GPL) web server scanner which performs comprehensive tests against web "
                "servers for multiple items, including over 6700 potentially dangerous files/programs, checks for "
                "outdated versions of over 1250 servers, and version specific problems on over 270 servers. It also "
                "checks for server configuration items such as the presence of multiple index files, HTTP server "
                "options, and will attempt to identify installed web servers and software. Scan items and plugins are "
                "frequently updated and can be automatically updated.")

parser.add_argument('-host', type=str, help='Target host', required=True)


parser.add_argument("-ask", choices=["yes","no","auto"], help="Whether to ask about submitting updates")
parser.add_argument("-Cgidirs", type=str, help="Scan these CGI dirs")
parser.add_argument("-Display", choices=["1","2","3","4","D","E","P","S","V"], help="Turn on/off display outputs")
parser.add_argument("-dbcheck", action="store_true", help="Check database and other key files for syntax errors")
parser.add_argument("-evasion", choices=["1","2","3","4","5","6","7","8","A","B"], help="Encoding technique")
parser.add_argument("-Format", choices=["csv","htm","nbe","txt","xml"], help="Save file format")
parser.add_argument("-IgnoreCode", action="store_true", help="Ignore Codes--treat as negative responses")
parser.add_argument("-id", type=str, help="Host authentication to use, format is id:pass or id:pass:realm")
parser.add_argument("-key", type=argparse.FileType('r'), help="Client certificate key file")
parser.add_argument("-list-plugins", action="store_true", help="List all available plugins, perform no testing")
parser.add_argument("-maxtime", type=int, help="Maximum testing time per host")
parser.add_argument("-mutate", choices=["1","2","3","4","5","6"], help="Guess additional file names")
parser.add_argument("-nolookup", action="store_true", help="Disables DNS lookups")
parser.add_argument("-nossl", action="store_true", help="Disables the use of SSL")
parser.add_argument("-no404", action="store_true", help="Disables nikto attempting to guess a 404 page")
parser.add_argument("-output", type=str, help="Write output to this file")
parser.add_argument("-Pause", type=str, help="Pause between tests (seconds, integer or float)")
parser.add_argument("-Plugins", type=str, help="List of plugins to run (default: ALL)")
parser.add_argument("-port", type=int, help="Port to use (default 80)")
parser.add_argument("-RSAcert", type=argparse.FileType('r'), help="Client certificate file")
parser.add_argument("-timeout", type=int, help="Timeout for requests (default 10 seconds)")

def main():
    subprocess.call(["nikto"] + sys.argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
