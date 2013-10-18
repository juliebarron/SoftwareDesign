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
        if has_no_e(word) and len(word) > 20: 
            pass #so that it doesn't affect my other functions 
            #print words

def avoids(word, forbidden):
    return not forbidden in word

#print avoids('hello', 'ap')

def uses_only(word, using):
    for letter in word:
        return not letter not in using

print uses_only('face holey', 'acefhlo')

def uses_all(word, required):
    return uses_only(required, word)

#print uses_all('haeli', 'aeiouy') something isn't right about this

if __name__ == '__main__':
    main()


