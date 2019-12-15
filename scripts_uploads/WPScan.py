import argparse
import sys
import subprocess
import os

#dependencia:
#sudo apt-get install ruby-full
#gem install wpscan

parser = argparse.ArgumentParser(description="WordPress Security Scanner by the WPScan Team.")
parser.add_argument('--url', help='The URL of the blog to scan', type=str, required=True)

at = parser.add_argument_group("Attack")

at.add_argument('-P', '--passwords', help='List of passwords to use during the password attack.', type=argparse.FileType('r'))
at.add_argument('-U', '--usernames', type=argparse.FileType('r'),
                        help='List of usernames to use during the password attack. (ex: "admin","admin,user"...')
at.add_argument('--wp-content-dir', type=str, help='The wp-content directory if custom or not detected, such as '
                                                       '"wp-content"')
at.add_argument('--wp-plugins-dir', type=str, help='The plugins directory if custom or not detected, such as '
                                                       '"wp-content/plugins"')
at.add_argument('--user-agent,', type=str, help='Custom User Agent')
at.add_argument('--random-user-agent,', action='store_true', help='Random User Agent')

at.add_argument('--password-attack', choices=('wp-login','xmlrpc','xmlrpc-multicall'),
                        help='Force the supplied attack to be used rather than automatically determining one. '
                             'Available choices: wp-login, xmlrpc, xmlrpc-multicall')

at.add_argument('--force', action='store_true', help='Do not check if the target is running WordPress')


con = parser.add_argument_group("Connection")
con.add_argument('--http-auth', type=str, help='login:password')
con.add_argument('-t', '--max-threads', type=int, help='The max threads to use')
con.add_argument('--throttle', type=int, help='Milliseconds to wait before doing another web '
                                                                  'request. If used, the max threads will be set to '
                                                                  '1.')
con.add_argument('--request-timeout', type=int, help='The request timeout in seconds')
con.add_argument('--connect-timeout', type=int, help='The connection timeout in seconds')
con.add_argument('--disable-tls-checks', action='store_true', help='Disables SSL/TLS certificate verification')


misc = parser.add_argument_group("Misc")
misc.add_argument('-f','--format', choices=["cli-no-colour", "cli-no-color", "cli", "json"],
                    help='Output results in the format supplied')
misc.add_argument('-v', help='Verbose mode', action='store_true')
misc.add_argument('--update', action='store_true', help='Update WPScan')
misc.add_argument('--api-key', type=str, help='The WPVulnDB API Token to display vulnerability data')






#parser.add_argument('-c', help='Color?', action='store_true')


def main():
    subprocess.call(["wpscan"] + sys.argv[1:])
    return 0



if __name__ == "__main__":
    sys.exit(main())
