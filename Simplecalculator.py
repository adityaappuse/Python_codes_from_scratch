def addition(val1,val2):
  print(val1+val2)
def subtraction(val1,val2):
 print(val1-val2)
def multiplication(val1,val2):
  print(val1*val2)
def division(val1,val2):
 print(val1/val2)
print("Type the values to be calculated:")
val1=int(input())
val2=int(input())
print("What operation would you like to perform?")
op=input()
if (op=='+'):
 addition(val1,val2)
elif (op=='-'):
 subtraction(val1,val2)
elif (op=='*'):
 multiplication(val1,val2)
elif (op=='/'):
 division(val1,val2)
else: 
 print("Oh no !!!It's a simple calculator stupid")
 
