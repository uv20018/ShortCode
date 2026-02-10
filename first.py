n=5
for i in range(n):
    print(" "*(n-i+1)+(2*i+1)*"*"+" "*(n-i+1),end="")
    print()


i=5
while i>0:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    i-=1
    print()


    for i in range(5,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()
        

        
