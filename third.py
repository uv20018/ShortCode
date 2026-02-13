#To remove duplicates
#Brute force 
# a=[2,2,4,5,6,6]
# print(set(a))


# l = [1,2,3,4,4,3,2]
# new_list = []

# for i in l:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

#Rotate the array by l digit
# l = [1,2,3,4,5]

# temp = l[0]
# for i in range(len(l)-1):
#     l[i] = l[i+1]
# l[len(l)-1] = temp
# print(l)

#Rotate the array by n 
# a=[1,2,3,4,5,6,7]
# temp=[]
# n=len(a)
# d=int(input("Enter the value"))
# d=d%n
# i=0
# for b in range(d):
#     temp.append(a[b])
# for j in range(d,len(a)):
#     a[i]=a[j]
#     i+=1
# for k in range(d):
#     a[i]=temp[k]
#     i+=1
# print(a)

# a=[1,0,2,3,2,0,0,4,5,1]
# temp=[]
# for i in range(len(a)):
#     if a[i]!=0:
#         temp.append(a[i])
# for i in range(len(temp)):
#     a[i]=temp[i]
# l=len(temp)
# for k in range(l,len(a)):
#     a[k]=0
# print(a)

a = [1,0,2,3,2,0,0,4,5,1]
j = 0   # position to place next non-zero
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[j] = a[j], a[i]
        j += 1
print(a)

    

        
    



        
        
        

