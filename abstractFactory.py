#AbstractFactory.py

class Dog:

    def speak(self):
        return "Woof"
    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Dog object"""
        return Dog()
    
    def get_food(self):
        """Return a Dog food object"""
        return "DogChow"

class Cat:

    def speak(self):
        return "Mew"
    def __str__(self):
        return "Cat"

class CatFactory:
    """Concrete Factory"""
    def get_pet(self):
        """Return a Cat object"""
        return Cat()
    
    def get_food(self):
        """Return a Cat food object"""
        return "Whiskas"
    

class PetStore:
    """PetStore house our Abstract Factory"""
    def __init__(self, pet_factory=None):
        self._pet_factory= pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects return by the Factory"""
        pet= self._pet_factory.get_pet()
        pet_food= self._pet_factory.get_food()
        
        print("Our pet is '{}'".format(pet))
        print("Our pet say hello by '{}'".format(pet.speak()))
        print("It's food is '{}'".format(pet_food))

    def set_factory(self, pet_factory):
        self._pet_factory= pet_factory

#Create a Concrete Factory
dog_factory= DogFactory()
#Create a pet store housing our abstract factory
shop= PetStore(dog_factory)
shop.show_pet()

#With cats
cat_factory= CatFactory()
factory= CatFactory()
shop= PetStore(cat_factory)
shop.show_pet()























