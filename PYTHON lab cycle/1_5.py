
def find_sum(n):
    if n == 0:
        return 0
    else:
        return n + find_sum(n - 1)

n = int(input("Enter the value for n: "))
result = find_sum(n)
print("The sum of numbers from 0 to n numbers is ", result)
