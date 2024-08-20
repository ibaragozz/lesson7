class Zoo():
    def __init__(self, name, animals, zookeeper, veterinarian):
        self.name = name
        self.animals = animals
        self.zookeeper = zookeeper
        self.veterinarian = veterinarian
        self.name = 'KoenigZoo'

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def get_animals(self):
        return self.animals

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.species = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return 'Twitt Twitt'

class Mammal(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        return 'Roar'

class Reptile(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def make_sound(self):
        return 'Hiss'

