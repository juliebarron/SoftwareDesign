def has_double_letter(word):
    index = 0
    while index < len(word)-1:
        if word[index] == word[index+1]:
            return True
        index = index + 1
    else:
        return False
def has_triple_double_letter(word):
    count = 0
    

print has_double_letter('hejhjkhllo')