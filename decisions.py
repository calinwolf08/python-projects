print "choose door 1 or 2"

first = raw_input("> ")

if first == "1":
	print "choose 1 or 2"
	sec = raw_input("> ")
	
	if sec == "1":
		print "chose 1 1"
	elif sec == "2":
		print "chose 1 2"
	else:
		print "chose 1 invalid"
elif first == "2":
	print "choose 1 2 or 3"
	sec = raw_input("> ")

	if sec == "1":
		print "chose 2 1"
	elif sec == "2":
		print "chose 2 2"
	elif sec == "3":
		print "chose 2 3"
	else:
		print "chose 2 invalid"
else:
	print "chose invalid"

