title='coding is easy'
try:
    print(tiele)
except NameError as msg:
    print(msg)
import math
num=int(input('please enter anumber to calculate factorial:'))
try:
    result=math.factorial(num)
    print(result)
except ValueError as msg:
    print(msg)
