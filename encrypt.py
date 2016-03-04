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
	option = raw_input("choose: ")
	while option != 'e' and option != 'd' and option != 'q':
		option = raw_input("choose: ")
	
	return option

def MethodMenu():
	print """
Which method do you want to use?
(c)aesarian fixed offset
(p)seudo-random offset
(s)ubstitution cipher
"""
	option = raw_input("choose: ")
	while option != 'c' and option != 'p' and option != 's':
		option = raw_input("choose: ")
	
	return option

def main():
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.?! \t\n\r"
	PrintDescription()
	
	while True:
		choice = StartMenu()
		if choice == 'q':
			break
		method_choice = MethodMenu()
		print "you chose: ", method_choice
		
	print "Good Bye"	

main()

