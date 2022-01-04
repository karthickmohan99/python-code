File=open('example.txt','r')
print('file name:',File.name)
print('file mode:',File.mode)
def getstatus(f):
    if(f.closed != False):
        return 'close'
    else:
        return 'open'
print(getstatus(File))
File.close()
print(getstatus(File))
