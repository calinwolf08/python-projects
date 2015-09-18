#iterable objects have __iter__ methods or __getItem__ which return iterators
#iterator has next method
#generators are iterators that only iterate once

def generator():
	for i in range(10):
		yield i

for item in generator():
	print item

def fibon(n):
	a = b = 1

	for i in range(n):
		yield a
		a, b=b, a + b
		#same as a = b, b = a+b ---> each side of comma applies to its corresponding item on other
		#side of the = sign

for x in fibon(20):
	print x

myString = "calin"

x = iter(myString)

for i in x:
	print i
