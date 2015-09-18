def greetMe(**kwargs):
	
	for key, value in kwargs.items():
		print "%s == %s !!!" % (key, value)

greetMe(name = "Calin")
