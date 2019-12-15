import argparse
import subprocess
import sys

# dependencia:
# apt-get install sqlmap

parser = argparse.ArgumentParser(
    description='sqlmap is an open source penetration testing tool that automates the process of detecting and '
                'exploiting SQL injection flaws and taking over of database servers. It comes with a powerful '
                'detection engine, many niche features for the ultimate penetration tester and a broad range of '
                'switches lasting from database fingerprinting, over data fetching from the database, to accessing '
                'the underlying file system and executing commands on the operating system via out-of-band '
                'connections.')
parser.add_argument('-u', type=str, help='Url to scan', required=True)

# request
req = parser.add_argument_group("Request")
req.add_argument('--data', type=str, help='Data string to be sent through POST')
req.add_argument('--cookie', type=str, help='HTTP Cookie header value')
req.add_argument('--random-agent', action="store_true",
                 help='Use randomly selected HTTP User-Agent header value')
req.add_argument('--tor', action="store_true", help='Use Tor anonymity network')

# injection
inj = parser.add_argument_group("Injection")
inj.add_argument('-p', type=str, help='Testable parameter(s)')
inj.add_argument('--dbms',
                 choices=['Firebird', 'HSQLDB', 'DB2', 'Informix', 'access', 'Microsoft SQL Server', 'MySQL',
                          'Oracle', 'PostgreSQL', 'MaxDB', 'SQLite', 'Sybase'], help='back-end DBMS')

# detection
det = parser.add_argument_group("Detection and Techniques")
det.add_argument('--level', type=int, choices=range(1, 6),
                 help='Level of tests to perform (1-5, default 1)')
det.add_argument('--risk', type=int, choices=range(1, 4), help='Risk of tests to perform (1-3, default 1)')

# Enumeration
enum = parser.add_argument_group("Enumeration")
enum.add_argument('-a', action='store_true', help='Retrieve everything')
enum.add_argument('-b', action='store_true', help='Retrieve DBMS banner')
enum.add_argument('--current-user', action='store_true', help='Retrieve DBMS current user')
enum.add_argument('--current-db', action='store_true', help='Retrieve DBMS current database')
enum.add_argument('--passwords', action='store_true', help='Enumerate DBMS users password hashes')
enum.add_argument('--tables', action='store_true', help='Enumerate DBMS database tables')
enum.add_argument('--columns', action='store_true', help='Enumerate DBMS database table columns')
enum.add_argument('--schema', action='store_true', help='Enumerate DBMS schema')
enum.add_argument('--dump', action='store_true', help='Dump DBMS database table entries')
enum.add_argument('--dump-all', action='store_true', help='Dump all DBMS databases tables entries')
enum.add_argument('-D', type=str, help='DBMS database to enumerate')
enum.add_argument('-T', type=str, help='DBMS database table(s) to enumerate')
enum.add_argument('-C', type=str, help='DBMS database table column(s) to enumerate')

# options
parser.add_argument('-v', type=int, default=1, choices=range(0, 7),
                    help='Verbosity level: 0-6 (default 1)')

# parser.add_argument('--batch', help='Do not require input.', action='store_true')

def main():
    subprocess.call(["sqlmap"]+sys.argv[1:]+["--batch"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
