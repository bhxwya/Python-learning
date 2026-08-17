class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print("Some Sound")

class Dog(Animal):
    def __init__(self,name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")
        
    def dog_details(self):
        print(f"Name  : {self.name}\nBreed : {self.breed}")
    
dog = Dog( "Bruno", "Labrador")
dog.dog_details()
dog.make_sound()