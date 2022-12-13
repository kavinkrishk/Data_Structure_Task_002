from functools import reduce

def is_even(n):
    return n%2==0

def is_odd(n):
    return n%2!=0

def update(n):
    return n*2

def even_plus(a,b):
    return a+b

def odd_plus(a,b):
    return a+b

nums = range(21)

evens = list(filter(is_even,nums))

odds = list(filter(is_odd,nums))

doubles1 = list(map(update,evens))

doubles2= list(map(update,odds))

even = reduce(odd_plus,doubles1)

odd = reduce(even_plus,doubles2)

print(evens)

print(odds)

print(doubles1)

print(doubles2)

print(even)

print(odd)
