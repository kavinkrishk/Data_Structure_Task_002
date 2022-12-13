#def add(a,b):
   # return(a+b)

#def sub(a,b):
    #return(a-b)

#def mul(a,b):
    #return(a*b)

#def div(a,b):
    #return(a//b)

print(int(input("""select your choice
1.add
2.sub
3.mul
4.div
""")))

a=int(input('enter number1'))

b=int(input('enter number2'))

choice=int(input('select your choice'))

if choice==1:
    print(add(a+b))

elif choice==2:
    print(sub(a-b))

elif choice==3:
    print(mul(a*b))

elif choice==4:
    print(div(a//b))

else:
    print("select correct choice")






