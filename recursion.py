# recursion

def recurse(x):
	if x == 0:
		return
	recurse(x-1)
	print "Bob", x

recurse(10)