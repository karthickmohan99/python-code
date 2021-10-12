i=1
while i<5:
    if i==4:
        break
    print('outer loop i=',i)
    i+=1
    j=1
    while j<5:
        if j==3 :
            print('breaks the loop')
            break
        print('\tinner loop j=',j)
        j+=1
        
