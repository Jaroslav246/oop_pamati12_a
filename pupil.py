class Pupil:
  __age=0
 
  
  def set_age(self, value: int):
    if value >=0:
      self.__age = value
    else: 
        print("Vecums nevar būt negatīvs")

        
  def get_age(self):
   return self.__age


pupil = Pupil()
pupil.set_age=(-1)
pupil.set_age=(10)
print(pupil.get_age())
