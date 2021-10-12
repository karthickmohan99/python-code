day=int(input('enter a day:'))
try:
    if day<50:
        raise ValueError('invalid day odu')
except  ValueError as msg:
    print('program found an error:',msg)

