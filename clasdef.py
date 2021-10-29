class Bird:
    '''a base for all critter properties'''
    count=0
    def __init__(self,chat):
        self.sound=chat
        Bird.count+=1
    def talk(self):
        print(Bird.count)
        print(self.sound)
        
harry=Bird('keech ,keech')
harry.talk()
harry.count
chick=Bird('kokoroko..')
chick.age='one week'
chick.talk()
print('age:',chick.age)
chick.age='three week'
print('age Now:',chick.age)
setattr(chick,'age','four week')
print('\nchick attributes:')
for atrr in dir(chick):
       if atrr[0]!='_':
         print(atrr,':',getattr(chick,atrr))
print('\nremove attribute:')
delattr(chick,'age')
print('check the atrribute',hasattr(chick,'age'))
