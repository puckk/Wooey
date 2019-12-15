import argparse
import subprocess
import sys

# dependencia:
# apt-get install nmap

parser = argparse.ArgumentParser(
    description="Nmap (\"Network Mapper\") is a free and open source (license) utility for network discovery and "
                "security auditing. Many systems and network administrators also find it useful for tasks such as "
                "network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap "
                "uses raw IP packets in novel ways to determine what hosts are available on the network, what "\
                "services (application name and version) those hosts are offering, what operating systems (and "
                "OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other "
                "characteristics. It was designed to rapidly scan large networks, but works fine against single "
                "hosts.")
parser.add_argument('host', type=str, help='Host IP address to scan')

hd = parser.add_argument_group("Host Discovery")
hd.add_argument('-sL', action="store_true", help="List Scan - simply list targets to scan.")
hd.add_argument('-sn', action="store_true", help="Ping Scan - disable port scan.")
hd.add_argument('-Pn', action="store_true", help="Treat all hosts as online -- skip host discovery.")
hd.add_argument('-n', action="store_true", help="Never do DNS resolution.")
hd.add_argument('-R', action="store_true", help="Always do DNS resolution.")
hd.add_argument('--traceroute', action="store_true", help="Trace hop path to each host.")
hd.add_argument('--dns-servers', type=str, help="Specify custom DNS servers.")
hd.add_argument('--system-dns', type=str, help="Use OS's DNS resolver.")

st = parser.add_argument_group("Scan Techniques")
st.add_argument('-sU', help='UDP Scan.', action="store_true")
st.add_argument('-sS', help='Syn Scan.', action="store_true")
st.add_argument('-sT', help='Connect() Scan.', action="store_true")
st.add_argument('-sA', help='ACK Scan.', action="store_true")
st.add_argument('-sW', help='Window Scan.', action="store_true")
st.add_argument('-sM', help='Maimon Scan.', action="store_true")
st.add_argument('-sN', help='TCP Null Scan.', action="store_true")
st.add_argument('-sF', help='FIN Scan.', action="store_true")
st.add_argument('-sX', help='XMas Scan.', action="store_true")
st.add_argument('-sO', help='IP Protocol Scan.', action="store_true")

pp = parser.add_argument_group("Ports and Order Scan")
pp.add_argument('-p', '--port', type=str, help='Port numbers to be scanned. Example: 22,1-100,1-65535.')
pp.add_argument('--exclude-ports', help='Exclude ports.', type=str)
pp.add_argument('--top-ports', help='Scan <number> most common ports.', type=int)
pp.add_argument('--port-ratio', help='Scan ports more common than <ratio>.', type=int)
pp.add_argument('-p-', help='Scan All ports.', action="store_true")
pp.add_argument('-F', help='Fast mode - Scan fewer ports than the default scan.', action="store_true")
pp.add_argument('-r', help='Scan ports consecutively - don\'t randomize.', action="store_true")

sv = parser.add_argument_group("Service/Version Detection")
sv.add_argument("-sV", help="Probe open ports to determine service/version info.", action="store_true")
sv.add_argument("--version-intensity", help="Set from 0 (light) to 9 (try all probes).", choices=range(0, 10))
sv.add_argument("--version-light", help="Limit to most likely probes (intensity 2).", action="store_true")
sv.add_argument("--version-all", help="Try every single probe (intensity 9).", action="store_true")
sv.add_argument("--version-trace", help="Show detailed version scan activity (for debugging).", action="store_true")

osd = parser.add_argument_group("OS Detection")
osd.add_argument("-O", help="Enable OS detection.", action="store_true")
osd.add_argument("--osscan-limit", help="Limit OS detection to promising targets.", action="store_true")
osd.add_argument("--osscan-guess", help="Guess OS more aggressively.", action="store_true")

ss = parser.add_argument_group("Script scan")
ss.add_argument("--script", type=str,
                help="<Lua scripts> is a comma separated list of directories, script-files or script-categories.")
ss.add_argument("--script-args", type=str, help="Provide arguments to scripts.")
ss.add_argument("--script-args-file", type=argparse.FileType('r'), help="provide NSE script args in a file.")
ss.add_argument("--script-trace", action="store_true", help="Show all data sent and received.")
ss.add_argument("--script-updatedb", action="store_true", help="Update the script database.")
ss.add_argument("--script-help", type=str, help="Show help about scripts.")


def main():
    subprocess.call(["nmap"] + sys.argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
