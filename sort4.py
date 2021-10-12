list=[[1,10],[2,9],[3,7]]
def sortBysec(element):
    return element[1]
list.sort(key=sortBysec)
print(list)
