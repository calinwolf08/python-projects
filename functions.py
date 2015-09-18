def print_two(*args):
	arg1, arg2 = args
	print "1: %r 2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "1: %r 2: %r" % (arg1, arg2)

def print_one(arg1):
	print  "arg1: %r" % arg1

def print_none():
	print "I got nothin"

print_two("Calin", "Wolf")
print_two_again("Calin", "Wolf")
print_one("First!")
print_none()
