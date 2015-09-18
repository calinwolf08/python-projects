#filter creates list for which a function is true

number_list = range(-5, 5)

less = list(filter(lambda x: x<0, number_list))
print less
