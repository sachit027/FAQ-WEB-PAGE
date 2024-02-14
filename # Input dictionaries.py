def add(x,y):
    return x+y
def sub(x,y):
    return x-y
print("mini calculator")
print("enter your choice")
print("1.add")
print("2.sub")
choice=input("enter your choice   :")
num1=float(input("enter num1: "))
num2=float(input("enter num2 :"))

if choice=='1':
    result=add(num1,num2)
elif choice=='2':
    result=sub(num1,num2)
else:
    result= "invalid"
print(f" the result is {result}")            
