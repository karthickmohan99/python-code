list1=[56,3,4,0,78,6,0]
for i in range(0,len(list1)-1):
    min_val=min(list1[i:])
    minval_index=list1.index(min_val,i)
    if list1[i]!= list1[minval_index]:
        list1[i],list1[minval_index]=list1[minval_index],list1[i]
    print(list1)
