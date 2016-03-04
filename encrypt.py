# encryption program

def PrintDescription():
	print """
This program encrypts and decrypts messages, using multiple encryption methods.
Input files must be in the same directory as this program.
Output files will be created in this same directory.
"""

def StartMenu():
	print """
Do you want to encrypt or decrypt?
(e)ncrypt
(d)ecrypt
(q)uit
"""
	choice = ''
	while choice != 'e' and choice != 'd' and choice != 'q':
	    choice = raw_input("choose: ")
	
	return choice

def main():
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! \t\n\r"
	PrintDescription()
	
	while True:
		option = StartMenu()
		print "option is ", option
		if option == 'q':
			break
	
	print "Good Bye"

main()

