class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self._name= name

    def speak(self):
        return "Woof"

class Cat:
    """A simple dog class"""
    def __init__(self, name):
        self._name= name

    def speak(self):
        return "Meow"

class Duck:
    """A simple duck class"""
    def __init__(self, name):
        self._name= name

    def speak(self):
        return "Cuak"

def get_pet(pet="dog"):
    """Teh factory method"""
    pets= dict(dog=Dog("Hope"), cat=Cat("Peace"), duck=Duck("Donald"))
    return pets[pet]


d= get_pet("dog")
print(d.speak())

c= get_pet("cat")
print(c.speak())



p= get_pet("duck")
print(p.speak())
