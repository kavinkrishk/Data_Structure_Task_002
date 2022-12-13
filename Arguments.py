# aruguments

#def sum( *b):
 #   c=0

  #  for i in b:
   #     c=c+i
   # print(c)

#sum(5,4,1,10,20,30,-10,40)


# keyword variable arguments

def person(name, **data):
    print(name)

    for i,j in data.items():

        print(i,j)

person('Kavin', Age = 28, City = 'Erode', mob = 9043625510)
