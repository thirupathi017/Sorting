#selection sort
a=[4,3,8,2,0]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        min=i
        if(a[j]<a[min]):
            min=j
    temp=a[j]
    a[min]=temp
    a[j]=a[min]
print(a)