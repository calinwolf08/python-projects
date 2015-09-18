def hi(name = "calin"):
	return "hi " + name

print hi()

greet = hi

print greet()

del hi

#print hi()

print greet()

del greet

def hi(name = "calin"):
	print "in hi"

	def greet():
		return "in greet"

	def welcome():
		return "in welcome"

	print greet()
	print welcome()
	print "in hi again"

	return greet

x = hi()

print x()

def thing(y):
	print y()

thing(x) 
