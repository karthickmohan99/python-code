while True :
    year=int(input('Enter a  year:'))
    if year%4==0:
     if year%100==0:
        if year%400==0:
            print('Given year is leap year')
        else:
            print('Given year is not aleap year')
     else:
         print('Given year is leap year')
    else:
        print('Given year is not a leap year')
    if year==0:
        break
