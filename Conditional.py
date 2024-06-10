list1 = ["Bineesh","Sreekesh","Hari","Abi","Sivanand"]

if "Hari" in list1:
    print("Name is present")
else:
    print("Name is not present")

list1.sort()
for n in list1:
    print(n, end=" ")
print("\n")
i=0
while i<len(list1):
    print(list1[i])
    i+=1

    