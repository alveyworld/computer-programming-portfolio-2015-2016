# simple calculator

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def div(x, y):
	if y == 0:
		return "undefined"
	return x / y
	
def mul(x, y):
	return x * y
	
	

def main():
	print "Welcome to my simple calculator"
	

	print div(5, 0)
	
main()