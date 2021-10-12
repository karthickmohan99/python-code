from datetime import*
Today=datetime.today()
print('starting countdown at:',Today.hour,':',Today.minute,':',Today.second,sep='')
from time import*
start_time=time()
struct=localtime(start_time)
i=5
while i>-1:
    print(i)
    i-=1
    sleep(1)
end_time=time()
struct3=localtime(end_time)
difference=round(end_time-start_time)
print('Runtime:',difference,'seconds')
print('Ending countdown at:',struct3.tm_hour,':',struct3.tm_min,':',struct3.tm_sec,sep='')
