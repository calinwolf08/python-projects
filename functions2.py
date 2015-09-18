from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "print whole file: \n"

print_all(current_file)

print "now rewind using seek"

rewind(current_file)

print "lets print each line"

x = 1

print_a_line(x, current_file)
x = x+1
print_a_line(x, current_file)
x = x+1
print_a_line(x, current_file)
