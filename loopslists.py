count = [1,2,3,4,5]
fruits = ["apples","oranges","pears","apricots"]
change = [1, "pennies", 2, 'dimes', 3, 'quarters']

for number in count:
	print "count:", number

for fruit in fruits:
	print "fruit:", fruit

for i in change:
	print "i:", i

elements = []

for i in range(0, 6): # goes 0 -> 5
	print "adding %d to list" % i
	elements.append(i)

for i in elements:
	print "element is", i
