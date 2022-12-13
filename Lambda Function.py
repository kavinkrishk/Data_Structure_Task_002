from functools import reduce

nums = range(10)

# or nums = [10,2,53,46,15,65,12,32,79]

evens = list(filter(lambda n : n%2==0,nums))

odds  = list(filter(lambda n : n%2!=0,nums))

doubles1 = list(map(lambda n : n*2,evens))

doubles2 = list(map(lambda n : n*2,odds))

even = reduce(lambda k,s : k+s,doubles1)

odd = reduce(lambda k,s : k+s,doubles2)

print(evens)

print(odds)

print(doubles1)

print(doubles2)

print(even)

print(odd)
