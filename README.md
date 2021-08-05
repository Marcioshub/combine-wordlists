# Combine Wordlists

Combine wordlist files, ensures they are all unique, and outputs it into a new_wordlist.txt file.

## Installation

pip install -r requirements.txt

## Usage

```bash
python3 combine.py wordlist1.txt wordlist2.txt wordlist3.txt
```

## Caveats

1. Make sure you do not rename the combine.py file, if you do you will also need
   to update the code.
2. Ensure the file paths to are correct before starting.
3. If you only add one wordlist file it will still copy all unique words into a new_wordlist.txt file.
4. The code uses a set() function for uniqueness, so the words will not be in order as they were read in.
5. When you create a new new_wordlist.txt it will override the old version.
