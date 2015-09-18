#map adds function to items in list
items = [1,2,3,4,5]

squared = []

for i in items:
	squared.append(i**2)

#same as

squared2 = list(map(lambda x: x**2, items))

for i in range(0,5):
	print "first: %d, sec: %d" % (squared[i], squared2[i])

def mult(x):
	return x*x

def add(x):
	return x+x

funcs = [mult, add]

for i in range(5):
	val = list(map(lambda x: x(i), funcs))
	print val
