class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction

class Rhinoceros(Animal):
    def __init__(self, name, food, habitat, reproduction, horn_length, skin_color):
        super().__init__(name, food, habitat, reproduction)
        self.horn_length = horn_length
        self.skin_color = skin_color

    def display_info(self):
        print(f"Name: {self.name}\nFood: {self.food}\nHabitat: {self.habitat}\nReproduction: {self.reproduction}")
        print(f"Horn Length: {self.horn_length}\nSkin Color: {self.skin_color}")
        print("------------------------------")

class Fish(Animal):
    def __init__(self, name, food, habitat, reproduction, fin_size, color):
        super().__init__(name, food, habitat, reproduction)
        self.fin_size = fin_size
        self.color = color

    def display_info(self):
        print(f"Name: {self.name}\nFood: {self.food}\nHabitat: {self.habitat}\nReproduction: {self.reproduction}")
        print(f"Fin Size: {self.fin_size}\nColor: {self.color}")
        print("------------------------------")

class Snake(Animal):
    def __init__(self, name, food, habitat, reproduction, length, venomous):
        super().__init__(name, food, habitat, reproduction)
        self.length = length
        self.venomous = venomous

    def display_info(self):
        print(f"Name: {self.name}\nFood: {self.food}\nHabitat: {self.habitat}\nReproduction: {self.reproduction}")
        print(f"Length: {self.length}\nVenomous: {self.venomous}")
        print("------------------------------")

# Contoh penggunaan
rhino = Rhinoceros("Rhinoceros", "Grass", "Land", "Viviparous", 30, "Gray")
rhino.display_info()

fish = Fish("Goldfish", "Fish Food", "Aquarium", "Oviparous", 5, "Gold")
fish.display_info()

snake = Snake("Python", "Rodents", "Forest", "Oviparous", 10, True)
snake.display_info()
