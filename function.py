#calling a function
def emobilis():
    print("This is my first function")
emobilis()
def calculatesquare():
    x=5
    y=8
    print(x*y)
calculatesquare()
def majina(fname, lname, age):
    print(fname + lname+ age)
majina("Brad ", "Lusalenge ", "54" )

def cars(name, type, numberplate):
    print(name + type + numberplate)
cars("Toyota ", "Corolla ","KCU 678L")
cars("Honda ","CRV ","KBF 538L")
cars("Subaru ","Impreza ","KDK 456Y")
cars("Mercedes ","S500 ","KDB 643S")
def maximum(a,b,c,d,e,f,g):
    return max(a,b,c,d,e,f,g)
result=maximum(5,15,67,0,97,89,45)
print(result)
#minimum
def minimum(k,l,m,n,o,p):
    return min(k,l,m,n,o,p)
result=minimum(89,345,231,456,73,5676,)
print(result)
#for numbers
def print_numbers(nambari):
    for i in range(nambari):
        print(i)
print(17)