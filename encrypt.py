# encryption program
import random

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
	
def MethodMenu():
	print """
Which method do you want to use?
(c)aesarian fixed offset
(p)seudo-random offset
(s)ubstitution cipher
"""
	choice = ''
	while choice != 'c' and choice != 'p' and choice != 's':
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
		method_option = MethodMenu()
		source_file = raw_input("What source file? ")
		dest_file = raw_input("What destination file? ")
		password = raw_input("What password? ")
		
		try:
			fin = open(source_file, "rb")
			fout = open(dest_file, "wb")
		except:
			print "Cannot read file"
			continue
		random.seed(password)
		
		
	
	print "Good Bye"

main()

