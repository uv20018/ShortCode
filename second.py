#Finding the largest element
l=[3,2,1,4,5]
largest=l[0]
for i in l:
    if(i>largest):
        largest=i
print(largest)

#Second largest element better solution
l=[3,2,5,4,5]
largest=l[0]
for i in l:
    if(i>largest):
        largest=i
print(largest)
sl=-1
for i in l:
    if(i>sl and i!=largest):
        sl=i
print(sl)


#optimal solution to find second largest
l=[1,2,3,4,5]
largest=l[0]
for i in range(1,5):
    if largest<l[i]:
        sl=largest
        largest=l[i]
print(largest)
print(sl)

#for second minimum
a=[1,2,3,4,5]
s=a[0]
for i in range(1,5):
    if a[i]<s:
        s=a[i]
print(s)

#Smallest and Second smallest by optimal approach
a=[1,2,3,4,5]
s=a[0]
ss=float('inf')
for i in range(1,5):
    if a[i]<s:
        ss=s
        s=a[i]
    elif a[i]<ss:
        ss=a[i]
print(s)
print(ss)

#Check array is sorted
is_sorted=True
l=[1,2,3,4,5]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        is_sorted=False
        break
if is_sorted:
    print("Sorted")
else:
    print("Not")



        

