original_array=[]
n=int(input("enter the range for original array:"))
for i in range(n):
    original_array.append(int(input(f"original_array[{i}]:")))
k=max(original_array)+1
count=[0]*k
for i in original_array:
    count[i]+=1
print(count)
for i in range(1,k):
    count[i]=count[i]+count[i-1]
print(count)
result=[0]*n
for i in range(n-1,-1,-1):
    value=original_array[i]
    count[value]-=1
    result[count[value]]=value 
print(result)
