class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return 'Canary makes Twitt Twitt'

class Mammal(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        return 'Lion makes roar'

class Reptile(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def make_sound(self):
        return 'Snake makes hiss'

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        pass

class Zookeeper(Worker):
    def feed_animal(self, animal):
        print(f'{self.name} is feeding {animal.name}')

class Veterinarian(Worker):
    def heal_animal(self, animal):
        print(f'{self.name} is healing {animal.name}')

import pickle

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Added {animal.name} to the zoo')

    def add_worker(self, worker):
        self.workers.append(worker)
        print(f'Added {worker.name} to the zoo')

    def feed_all_animals(self):
        for worker in self.workers:
            if isinstance(worker, Zookeeper):
                for animal in self.animals:
                    worker.feed_animal(animal)

    def save_to_file(self, filename):
        """Сохраняет текущее состояние зоопарка в файл."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Zoo state saved to {filename}")

    @staticmethod
    def load_from_file(filename):
        """Загружает состояние зоопарка из файла."""
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Zoo state loaded from {filename}")
        return zoo

    def heal_all_animals(self):
        for worker in self.workers:
            if isinstance(worker, Veterinarian):
                for animal in self.animals:
                    worker.heal_animal(animal)

# Создание объектов животных
bird = Bird("Canary", 3, "Yellow")
mammal = Mammal("Lion", 5, "Large")
reptile = Reptile("Snake", 2, "Desert")

# Создание объектов сотрудников
zookeeper = Zookeeper("John", 35)
vet = Veterinarian("Emily", 40)

# Создание зоопарка
zoo = Zoo("KoenigZoo")

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_worker(zookeeper)
zoo.add_worker(vet)

# Демонстрация полиморфизма
animal_sound(zoo.animals)

# Кормление всех животных
zoo.feed_all_animals()

# Лечение всех животных
zoo.heal_all_animals()

# Сохранение состояния зоопарка в файл
zoo.save_to_file("zoo_state.pkl")

# Восстановление состояния зоопарка из файла
# loaded_zoo = Zoo.load_from_file("zoo_state.pkl")
