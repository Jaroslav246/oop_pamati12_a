class Animal:
    legs=4
    tail=1

    def voice(self):
        print('kaut-kāda skaņa')

class CAt(Animal):
    def cat_voice(self):
        print('Mjau')

class Dog(Animal):
    def dog_voice(self):
        print('Gav')

class Bull(Animal):
    def bull_voice(self):
        print('Muuu')


anim=Animal()
anim.voice()
cat1,cat2=Cat(), Cat()
dog1, dog2=Dog(), Dog()
bull1, bull2=Bull(), Bull()

cat1.cat_voice()
cat2.cat_voice()
dog1.dog_voice()
dog2.dog_voice()
bull1.bull_voice()
bull2.bull_voice()

farm+band=[cat1, cat2, dog1, dog2, bull1, bull2]
for i in farm_band:
    i.voice