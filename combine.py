import sys
from termcolor import colored

def main(argv):
    new_wordlist = set()

    if len(argv) <= 1:
        print(colored("Error: You need at least one file", "red"))
        sys.exit();

    for i in argv:
        if i == "combine.py":
            continue
        file1 = open(i, 'r')
        lines = file1.readlines()
        for line in lines:
            if line.rstrip("\n") in new_wordlist:
                print(colored(line.rstrip("\n") + " " + "is already in the wordlist", "red"))
            else:
                new_wordlist.add(line.rstrip("\n"))
                print(colored(line.rstrip("\n") + " " + "added to wordlist", "green"))
        file1.close()

    with open("new_wordlist.txt", 'w') as nwl:
        for i in new_wordlist:
            nwl.write(i + "\n")

    print(colored("new_wordlist.txt has been saved!", "cyan"))

if __name__ == "__main__":
    main(sys.argv)