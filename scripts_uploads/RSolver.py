from argparse import ArgumentParser,FileType
import subprocess
import sys


#Var auxs
parser = ArgumentParser("RSolver. SYPER Tool for RSA Challenges")

argumentsinputs = parser.add_argument_group('ARGUMENTS INPUTS')
filesinputs = parser.add_argument_group('FILE INPUTS')
private = parser.add_argument_group('INPUT PRIVATE PARTIAL KEYS')
ciphertexts=parser.add_argument_group('CIPHERTEXT INPUTS')
debuggroup = parser.add_argument_group('General')


# #Files input
filesinputs.add_argument("--publickey",  dest="pem", type=FileType('r'), nargs='*', help="Path of Public(s) key(s) in PEM format (space separated)")
filesinputs.add_argument("--inputfile", dest="file", type=FileType('r'), help="file with the challenge data in decimals/hex")

private.add_argument("--partialkey", "-pk", dest="partialkey", help="Input base64 priv key filling with * the first or last character")
private.add_argument("--partialkeyfile", "-pkf", dest="partialkeyfile",  type=FileType('r'),  help="Filepath with base64 priv key filling with * the first or last character")

# Arguments line input
argumentsinputs.add_argument("-p", dest="p", help="Input p value in decimal/hex")
argumentsinputs.add_argument("-q", dest="q", help="Input q value in decimal/hex")
argumentsinputs.add_argument("-n", dest="n", help="Input n value in decimal/hex")
argumentsinputs.add_argument("-e", dest="e", help="Input e value in decimal/hex")
argumentsinputs.add_argument("-f", dest="phi", help="Input phi value in decimal/hex")
argumentsinputs.add_argument("-d", dest="d", help="Input d value in decimal/hex")
argumentsinputs.add_argument("-dp", dest="dp", help="Input dp value in decimal/hex")
argumentsinputs.add_argument("-dq", dest="dq", help="Input dq value in decimal/hex")
argumentsinputs.add_argument("-qinv", dest="qinv", help="Input qinv value in decimal/hex")
argumentsinputs.add_argument("-blind", dest="blind", action="store_true", help="Set this for blind RSA is possible (Oracle Attack)")
argumentsinputs.add_argument("-ucp", dest="ucp", help="Set this for blind RSA. ucp value")

ciphertexts.add_argument("-c", dest="c", help="Input c value in decimal/hex")
ciphertexts.add_argument("--c64file", dest="c64file", type=FileType('r'), nargs='*', help="Input crypted(s) file(s) in base64")
ciphertexts.add_argument("--cfile", "-x", dest="cryptfile", type=FileType('rb'), nargs='*', help="Input encrypted/s file/s")
ciphertexts.add_argument("-c64", dest="c64",  help="Input c in base64")

#Debug
debuggroup.add_argument("--debug", dest="debug", help="Debug mode")
debuggroup.add_argument("--timeout", dest="timeout", help="Timeout for each script, default 120segs")
debuggroup.add_argument("--scripts", dest="scripts", help="Optional: Launch only custom scripts. Valids are: n_is_prime,multin,tokyo,zfermat,boneh_durfee,getpqefromdpdqqinv,withdp,common_modulus,common_prime,yafu,ces1,zmultiprimeYafu,wiener,pyqdadod,blind,wiener2,hastad,hastadwithouthE,factordb,lowq,wiener3,boneh_durfee", type=str)


def main():
    subprocess.call(["rsolver"]+sys.argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
