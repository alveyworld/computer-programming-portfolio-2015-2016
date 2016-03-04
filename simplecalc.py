# Program that is a simple calculator

def leopard():
	print "rock on"

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def mod(a, b):
	return a % b



def main():
	print "Welcome to my simple calculator"
	n1 = int(raw_input("Enter a number: "))
	n2 = int(raw_input("Enter a number: "))
	
	print mul(n1, n2)
	print add(n1, n2)

main()