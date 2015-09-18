from sys import argv

script, filename = argv

print "were going to erase %s" % filename

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating file..."
target.truncate()

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

target.close()

target = open(filename)
print target.read()
