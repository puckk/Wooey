import argparse
import subprocess
import sys
import itertools

parser = argparse.ArgumentParser(
  description='Make a Dictionary with the words you want')
parser.add_argument('words', type=str, help='Words tu make the dictionary')


def append_list(f, words, delim):
    for word in words:
        f.write(delim.join(word)+"\n")


def main():
    a = parser.parse_args()
    words = a.words
    with open("output_corto.txt", "w") as f:
        lists = [words,
                 [w for w in itertools.permutations(words, 2)],
                 [w for w in itertools.permutations(words, 3)]]
        delims = ["", " ", ",", ";"]
        for words in lists:
            for delim in delims:
                append_list(f, words, delim)

        subprocess.check_output("john -wordlist:`pwd`/output_corto.txt -rules:Single -stdout > `pwd`/output_largo.txt",
                            shell=True)


    return 0




if __name__ == "__main__":
    sys.exit(main())
