states = {
	'Oregon': "OR",
	"Washington": 'WA',
	'California': 'CA',
	"New York": 'NY'
}

cities = {
	'CA':'San Francisco',
	'WA':'Seattle',
	'OR':'Portland',
}

cities['NY'] = 'New York'

print '-' * 10

print "NY state has: ", cities["NY"]
print "OR state has: ", cities["OR"]

print '-' * 10

print "Washington's abbreviation is: ", states['Washington']
print "California's abbreviation is: ", states['California']

print "Washington has ", cities[states["Washington"]]
print "California has ", cities[states['California']]

print '-' * 10

for state, abbrev in states.items():
	print "%s has the city %s" % (state, abbrev)

print '-' * 10

state = states.get("Texas")

if not state:
	print "Sorry, no Texas"

city = cities.get("TX", "Sorry no texas")

print "city for TX: ", city
