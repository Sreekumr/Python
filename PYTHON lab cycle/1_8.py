factorial = {}

def factorials(n):
    if n in factorial:
        return factorial[n]
    
    if n == 0 or n == 1:
        factorial[n] = 1
    else:
        factorial[n] = n * factorials(n - 1)
    
    return factorial[n]


number = 5
fact = factorials(number)
print("The factorial of ",number ,"is ", fact)
print("Factorial cache:", factorial)
