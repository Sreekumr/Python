
sum = 0
count = 0
for i in range(100, 200):
    if i%7==0:
        sum = sum + i
        count= count+1

print("Sum of numbers between 100 and 200 that are divisible by 7 is", sum)
print("Number btw 100 and 200 that are divisible by 7 is ",count)