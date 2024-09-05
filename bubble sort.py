#bubble sort=ascending order
n=int(input('enter a number:'))
a=[]
for i in range(n):
    a.append(int(input())) 
for i in range(0,n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
            
