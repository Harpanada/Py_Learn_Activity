#Class
class Animals:
    #atribut instance
    def __init__(self, name, species, age):
        #Constructor
        self.name = name #attribute
        self.species = species  #attribute
        self.age = age     #attribute

    #Method
    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age} years")


#Instance/Object
animal_1 = Animals("Leo", "Lion", 5)


