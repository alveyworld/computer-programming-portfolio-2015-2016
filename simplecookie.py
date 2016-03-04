# today we are making cookies

def has_cookie():
	try:
		cookie = open("zcookie.txt", "r")
		cookie.close()
		return True
	except:
		return False
		
def set_cookie(name, email):
	cookie = open("zcookie.txt", "w")
	cookie.write(name + "\n")
	cookie.write(email + "\n")
	cookie.close()

def greet():
	try:
		cookie = open("zcookie.txt", "r")
		lines = cookie.readlines()
		name = lines[0].strip()
		email = lines[1].strip()
		print "Welcome %s! Nice to see you again, is your email still %s?" % (name, email)
		cookie.close()
	except:
		print "Welcome! I don't know you yet."
		
def show_instructions():
	print "Hello, please enter your name: "
	name = raw_input()
	print "now enter your email: "
	email = raw_input()
	return (name, email)

def main():
	if has_cookie():
		greet()
	
	name, email = show_instructions()
	set_cookie(name, email)
	
	print "Thank you. Have a nice day %s!" % (name)

main()


