# encryption program
import random

def Caesarian(fin, fout, encrypt_or_decrypt_choice, alphabet):
    # Determine the offset by generating a random number in the correct range.
    # This will be the same random number, if the password sent to random.seed is the same.
    offset = random.randrange(1,len(alphabet))
    if encrypt_or_decrypt_choice=='d':
        offset = -offset
    print "Using the secret offset of", offset

    # Read every line of the input file.
    for line1 in fin:
        # Alter each character of the line1, putting the result into line2.
        line2 = ""
        for c in line1:
            if c in alphabet:
                pos1 = alphabet.find(c)
                pos2 = (pos1+offset)%len(alphabet)
                line2 += alphabet[pos2]
        # Write each resulting line2 to the output file.
        fout.write(line2)

def PseudoRandom(fin, fout, encrypt_or_decrypt_choice, alphabet):
	pass

def Sustitution(fin, fout, encrypt_or_decrypt_choice, alphabet):
	pass

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
		
		print "Enter an input file name: "
		source_file = raw_input()
		print "Enter an output file name: "
		destination_file = raw_input()
		print "Enter your password: "
		password = raw_input()
		
		try:
			fin = open(source_file, "rb")
		except:
			print "That file doesn't exist"
			continue
		fout = open(destination_file, "wb")
		random.seed(password)
		
		if method_choice == "c":
			Caesarian(fin, fout, choice, alphabet)
		elif method_choice == "p":
			PseudoRandom(fin, fout, choice, alphabet)
		else:
			Substitution(fin, fout, choice, alphabet)
		
		
	print "Good Bye"	
		

main()

