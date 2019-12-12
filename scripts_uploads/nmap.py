import argparse
import sys
import subprocess
import os

#dependencia:
#apt-get install nmap

parser = argparse.ArgumentParser(description="Nmap port scanner script.")
parser.add_argument('host', type=str, help='Host IP address to scan')


hd = parser.add_argument_group("Host Discovery")
hd.add_argument('-sL', action="store_true", help="List Scan - simply list targets to scan")
hd.add_argument('-sn', action="store_true", help="Ping Scan - disable port scan")
hd.add_argument('-Pn', action="store_true", help="Treat all hosts as online -- skip host discovery")

st = parser.add_argument_group("Scan Techniques")
st.add_argument('-sU', help='UDP Scan', action="store_true")
st.add_argument('-sS', help='Syn Scan', action="store_true")
st.add_argument('-sT', help='Connect() Scan', action="store_true")
st.add_argument('-sA', help='ACK Scan', action="store_true")
# st.add_argument('-sA', help='ACK Scan', action="store_true")
st.add_argument('-sW', help='Window Scan', action="store_true")
st.add_argument('-sM', help='Maimon Scan', action="store_true")
st.add_argument('-sN', help='TCP Null Scan', action="store_true")
st.add_argument('-sF', help='FIN Scan', action="store_true")
st.add_argument('-sX', help='XMas Scan', action="store_true")
st.add_argument('-sO', help='IP Protocol Scan', action="store_true")


parser.add_argument('-p', '--port', type=str, help='Port numbers to be scanned. Example: 22,1-100,1-65535')
# parser.add_argument('-sU', help='UDP scan', action="store_true")
# parser.add_argument('-A', help='OS detection and version', action="store_true")
# parser.add_argument('-v', help='Increase verbose', action="store_true")
# parser.add_argument('-sL', help='List scan', action="store_true")
# parser.add_argument('-sn', help='Ping scan', action="store_true")
# parser.add_argument('-sV', help='Fingerprinting', action="store_true")
# parser.add_argument('-F', help='Fast', action="store_true")
# parser.add_argument('-f', help='Fragment', action="store_true")
parser.add_argument('-p-', help='Scan All ports', action="store_true")


def main():
    subprocess.call(["nmap"] + sys.argv[1:])
    return 0



if __name__ == "__main__":
    sys.exit(main())
