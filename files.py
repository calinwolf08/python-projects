from sys import argv

script, filename = argv

txt = open(filename)

print "file is:", filename
print txt.read()

print "type filename again"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
