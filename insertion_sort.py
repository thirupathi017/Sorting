'''Algorithm
1.take first element in array is sorted remaining is unsorted
2.take first element in unsorted part(u1) and compare it with sorted part elements(s1).
3.if (u1<s1) then insert at correct position else leave it.
4.repeat util sorted.'''
def insertion_sort(li):
    for i in range(1,len(li)):
        current_elem=li[i]
        pos=i
        while(current_elem<li[pos-1] and pos>0):
            li[pos]=li[pos-1]
            pos=pos-1
        li[pos]=current_elem
li=[1,5,3,8,2]
insertion_sort(li)
print(li)