def test_double_letters(word):
    index = 0
    count = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            count += 1
            if count == 3:
                return True
            index += 2
        else:
            count = 0
            index += 1
    return False

def find_double_letters():
    for line in open('words.txt'):
        word = line.strip()
        if test_double_letters(word):
            print word 

#print 'All words with three consecutive double letters.'
#print find_double_letters()

def string_fill(i, len):
    return str(i).zfill(len)

def are_reversed(i, j):
    """returns True if integers i & j are the reveerse
    of each other."""

    return string_fill(i, 2) == string_fill(j, 2) [::-1]

def num_instances(diff, flag=False):
    daughter = 0
    count = 0 
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count += 1 
            if flag:
                print daughter, mother
         if mother > 120:
            break
        daughter += 1
    return count

def check_diffs():
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print diff, n
        diff += 1

print 'diff #instances'
check_diffs()

print
print 'daughter mother'
num_instances(18, True)
