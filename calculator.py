


num1  = int(input("Enter Number 1:"))
num2  = int(input("Enter Number 2:"))
op = input("Enter the operation: ")
res =0
if op== '+' :
  res = num1+ num2
elif op=='-':
        res = num1 - num2
elif op=='/':
             res= num1/num2
elif op=='*':
                res= num1*num2
else :
              print("Invalid operation")

print("Result=",res)

    