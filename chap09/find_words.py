"""Test code for find_words.py.

Author: Allen B. Downey
"""

def has_no_e(s): 
    return not 'e' in s

def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        # only print palindromes
        return uses_all(word, 'aeiouy')
    print word
            
            

def avoids(word, forbidden):
    return not forbidden in word



def uses_only(word, using):
    for letter in word:
        if letter not in using:
            return False

        return True



def uses_all(word, required):
    for letter in required:
        if letter not in word: 
            return False

        return True



if __name__ == '__main__':
    main()


