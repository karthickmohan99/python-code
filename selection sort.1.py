list1=[56,3,4,78,6,0]
for i in range(len(list1)):
    min_val=min(list1[i:])
    minval_index=list1.index(min_val)
    list1[i],list1[minval_index]=list1[minval_index],list1[i]
print(list1)
