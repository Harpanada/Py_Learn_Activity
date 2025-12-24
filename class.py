

#Class Constructor
class Mobil:
  def __init__(self,colour,speed,brand,engine):
        self.colour=colour
        self.speed=speed
        self.brand=brand
        self.engine=engine


def displayCar(x):
    print(f"The Car is: {x.brand}. {x.engine} Engine. Speed:{x.speed}km/h. Colour:{x.colour}")




car_1=Mobil("White",280,"BMW M4","INLINE 6-CYLINDER")
car_2=Mobil("Green",300 , "Aston Martin DB12", "V8 Twin Turbo")
displayCar(car_1)
displayCar(car_2)





