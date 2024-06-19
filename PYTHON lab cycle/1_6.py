
def reverseNum(num):
    rev = 0
    while num > 0:
        rev *= 10
        rev += (num % 10)
        num = num // 10
    return rev

def isPalindrome(number):
    isPal = True
    if number != reverseNum(number):
        isPal = False
    return isPal


n = int(input("Enter Number: "))
n += reverseNum(n)
while not isPalindrome(n) : n += reverseNum(n)
print(n)
