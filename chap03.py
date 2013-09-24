#Julie Barron
def top_part():
	print '+ - - - - + - - - - +'

def inside_part():
	print '|         |         |'

def box(rows):
	top_part()
	for j in range(rows):
		for i in range(4):
			inside_part()
		top_part()

box(2)