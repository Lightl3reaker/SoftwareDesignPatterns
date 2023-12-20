
class Computer():
    def __init__(self,brand,processor,memory,storage,graphics_card):
        self.brand=brand
        self.processor=processor
        self.memory=memory
        self.storage=storage
        self.graphics_card=graphics_card
    def __str__(self):
        return f"{self.brand} Computer-{self.processor},{self.memory}RAM,{self.storage}Storage,{self.graphics_card}GPU"

class ComputerBuilder:
    def set_brand(self,brand):
        pass
    def set_processor(self,processor):
        pass
    def set_memory(self,memory):
        pass
    def set_storage(self,storage):
        pass
    def set_graphics_card(self,graphics_card):
        pass
    def getcomputer(self):
        pass

class ConcreteComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer=Computer("default","default","default","default","default")
    def set_brand(self,brand):
        self.computer.brand=brand
        return self
    def set_processor(self, processor):
        self.computer.processor=processor
        return self
    def set_memory(self, memory):
        self.computer.memory=memory
        return self
    def set_storage(self, storage):
        self.computer.storage=storage
        return self
    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card=graphics_card
        return self
    def getcomputer(self):
        return self.computer

class Director():
    def construct(self,builder):
        return builder.set_brand("").set_processor("i9-8thgen").set_memory("16GB").set_storage("1TB").set_graphics_card("Navidia").getcomputer()
    

builder=ConcreteComputerBuilder()
director=Director()
computer=director.construct(builder)
print(computer)