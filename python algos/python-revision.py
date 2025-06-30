#dictionary
aliens = {'color': 'green', 'points': 5}
print(aliens['color'])
aliens['position'] = 10
print(aliens)
aliens['color'] = 'red'
print(aliens)

for k, v in aliens.items(): #items call pairs in dictionary
    print(k)
    print(v)

for names in aliens.keys(): #get key names, .values() to get values of keys
    print(names)

def number(var: int) -> int:
    """
    Type annotations: specifies input of a function and return type
    """
    return var

print(number(5))

a = [1,2,3]
b = a[:] #cloning the list, not aliasing, a and b are two separate lists

# list comprehension
c = [n for n in range(5)]
print(c)

# Other stuff to recap: unit testing, advanced OOP, lambda functions, File IO

#lambda functions
square = lambda x: x**2
print(square(5))

#map function: applies a function to each item of an iterable
l1 = [2,3,4]
l2 = list(map(square, l1))
print(l2)