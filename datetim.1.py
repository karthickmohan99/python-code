from datetime import*
Today=datetime.today()
print(Today)
Tuple=['year','month','day','hour','minute','second','microsecond']
for atr in Tuple:
    print(atr,':\t',getattr(Today,atr))
print('getatt:',getattr(Today,'hour'))    
print('Time:',Today.hour,':',Today.minute,sep='')
day=Today.strftime('%A')
month=Today.strftime('%B')
print('Date:',day,month,Today.day)
