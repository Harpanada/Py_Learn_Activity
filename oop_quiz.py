
#Parent class
class Animal:
    def __init__(self, name,age,species):
        self.name = name
        self.age = age
        self.species = species

  
#Child class
class Cat(Animal):
    def deskripsi(self):
      return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meow!"
    

#Instance of Cat class
myCat= Cat("Neko", 3, "Persian")
