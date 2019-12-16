import argparse
import subprocess
import sys

# dependencia:
# apt-get install sqlmap

parser = argparse.ArgumentParser(
    description='Solver for RSA exercises.')

# request

def main():
    subprocess.call(["sqlmap"]+sys.argv[1:]+["--batch"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
