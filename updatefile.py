text='the political slogan "workers of the world unite!"\n is from the communist manifesto.'
print(text.find('w'))
with open('update.txt','w')as file:
    file.write(text)
    print('\n',file.closed)
print('\n',file.closed)
with open('update.txt','r+')as file:
    Text=file.read()
    print('\n',Text)
    print('\nposition of file:',file.tell())
    file.seek(33)
    print('\nposition of file:',file.tell())
    file.write('all lands')
    file.seek(61)
    file.write('the tombstone of karlmarks')
    file.seek(0)
    print('\n',file.read())
    
