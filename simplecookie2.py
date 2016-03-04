# simple cookie program
def has_cookie():
	try:
		cookie = open("zcookie.txt", "r")
		cookie.close()
		return True
	except:
		return False

def set_cookie(name, email):
	cookie = open("zcookie.txt", "w")
	cookie.write(name+"\n")
	cookie.write(email+"\n")
	cookie.close()

def greet():
	try:
		cookie = open("zcookie.txt", "r")
		lines = cookie.readlines()
		name = lines[0].strip()
		email = lines[1].strip()
		print "Welcome back %s! Your email is %s" % (name, email)
		cookie.close()
	except:
		print "Welcome!"
		
		
def show_instructions():
	print "Hello, enter your name: "
	name = raw_input()
	print "Enter your email: "
	email = raw_input()
	
	return (name, email)

def main():
	if has_cookie():
		greet()
	else:
		print "Welcome!"
	
	name, email = show_instructions()
	set_cookie(name, email)
	
	print "Thank you %s, have a nice day." % (name)
	
main()


