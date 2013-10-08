def rotate_word(string, integer):
    word = ''

    for letter in string:
        n = ord(letter) + integer
        s = chr(n)
        word += s 
    return word

        

print rotate_word('cheer', 7)