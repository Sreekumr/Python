
units = int(input("Enter the Units: "))

bill = 0
if units <= 200:
    bill = units * 0.5
elif units <= 400:
        bill = 200 * 0.50 + (units - 200) * 0.65
elif units <= 600:
        bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
else:
        bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00
    
   
if bill > 400:
        bill *= 1.15
      
if bill < 100:
        bill = 100

print("The total Bill amount: ",bill)