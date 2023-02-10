#if statement
x=1
marks=49
grade=2000
shoeprice=6000
if(x>0):
    print("The number is positive")
#if ...else statement
if(marks>=60):
    print("you have passed the exam")
else:
    print("You have failed your exam")

#if..elif.. else statement (elif= else if)
if(grade<=29 and grade>=0):
    print("You failed")
elif grade>=30 and grade<=49:
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("Wrong grade entered")

shoeprice=500
if(shoeprice==600):
    print("I buy them")
if(shoeprice<600 and shoeprice<=500):
    print("Nitajikaza ninunue")
if(shoeprice==0 and shoeprice<999) :
    print("Nitanunua")