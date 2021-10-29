class Duck:
    def talk(self):
        print('duck says:quack')
    def coat(self):
        print('duck wears:feather')
class Mouse:
    def talk(self):
        print('mouse says:squeek')
    def coat(self):
        print('mouse wear:fur')
def describe(object):
    object.talk()
    object.coat()
donald=Duck()
micky=Mouse()
describe(donald)
describe(micky)
