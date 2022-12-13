email = (input("enter tha correct mail address"))
phonenum = (input("enter your phone number"))

len(email)

len(phonenum)

for i in email:
    i = 15
    if i>len(email):
        print(email,"@gmail.com")
        break
    else:
        print("invaild address")
        break

for k in range(10):
    k = int(len(phonenum))
    if k==10:
        print(phonenum)
        break

    elif k<10:
        print("should fill 10 numbers")
        break

    else:
        print("enter corrct numbers")
        break

