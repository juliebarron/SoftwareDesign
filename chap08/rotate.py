def rotate_word(s, n):
    word = ''

    for letter in s:
        u = ord(letter) + n
        s = chr(u)
        word += s 
    return word

        

print rotate_word('cheer', 7)