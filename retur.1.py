def sum(a,b):
    return a+b
total=sum(4,1)
print(total)

num=input('enter a number:')
def square(num):
    if not num.isdigit():
        return 'invalid entry'
    num=int(num)
    return num*num
print(square(num))

def sum(a,b):
    if a<5:
        return
    return a+b

total=sum(4,6)
print(total)
