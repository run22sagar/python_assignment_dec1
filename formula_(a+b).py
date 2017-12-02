def LHS(a,b):
    c=(a+b)**2
    return c
def RHS(a,b):
    c=(a**2)+(2*a*b)+(b**2)
    return c


num1=int(input("Enter value of a"))
num2= int(input ("Enter value of b"))


X =LHS(num1,num2)
Y =RHS(num1,num2)

if X==Y:
      print("LHS=RHS Hence Proved")
else :
    print("LHS is not equals to RHS")
