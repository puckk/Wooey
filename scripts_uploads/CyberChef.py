import argparse
import subprocess
import sys
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(
  description='Download the latest version of Cyberchef')



def main():
    a = requests.get("https://gchq.github.io/CyberChef/")
    soup = BeautifulSoup(a.text, 'html.parser')
    url = "https://gchq.github.io/CyberChef/"+soup.find("a")["href"]
    subprocess.check_output("wget {}".format(url), shell=True)
    return 0




if __name__ == "__main__":
    sys.exit(main())
