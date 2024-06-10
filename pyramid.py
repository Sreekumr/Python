
start= int(31/2)
end= int(31/2-1)

for i in range(0,16):
    for j in range(i):
            if j in range(start,end):
                  print("*",end="")
            else :print(" ",end="")
    start -= 1
    end += 1
    print()
        
    

