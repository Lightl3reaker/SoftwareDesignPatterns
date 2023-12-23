class House:
    def __init__(self):
        self.number_of_room=0
        self.number_of_bathroom=0
        self.has_garage=False
        self.has_garden=False
    def __str__(self):
        return f"House ---> {self.number_of_room} room, {self.number_of_bathroom} bathroom, Garden : {self.has_garden}, Garage : {self.has_garage}"

class HouseBuilder:
    def __init__(self):
        self.house=House()
    def set_room(self,room):
        self.house.number_of_room=room
        return self
    def set_bathroom(self,bathroom):
        self.house.number_of_bathroom=bathroom
        return self
    def set_garage(self):
        self.house.has_garage=True
        return self
    def set_garden(self):
        self.house.has_garden=True
        return self
    def bulid_house(self):
        return self.house

builder1=HouseBuilder()
builder1.set_room(5).set_bathroom(2).set_garden()
print(builder1.bulid_house())