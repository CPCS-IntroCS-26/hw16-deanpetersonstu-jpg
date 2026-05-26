class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        print(f"{Animal.name} says Grrr")

    def move(self):
        print(f"{Animal.name} Runs")

    def describe(self):
        print(f"{Animal.name}: is a {Animal.age} that makes this sound: {Animal.sound}")

    def __str__(self):
        return f'name: {self.name}\n' \
        f'age: {self.age}\n' \
        f'breed: {self.sound}'


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Woof!")
        self.breed = breed    
    
    def speak(self):
        print(f"{self.name} says Woof")

    def move(self):
        print(f"{self.name} sprints")

    def describe(self):
        print(f"{self.name} is a {self.age} year old {self.breed}")

    def __str__(self):
        return f'name: {self.name}\n' \
        f'age: {self.age}\n' \
        f'breed: {self.breed}'


class Bird(Animal):
    def __init__(self, name, age, beak):
        super().__init__(name, age, "Chirp")
        self.beak = beak    
    
    def speak(self):
        print(f"{self.name} chirps")

    def move(self):
        print(f"{self.name} flys")

    def describe(self):
        print(f"{self.name} is a {self.age} year old bird with a {self.beak}")

    def __str__(self):
        return f'name: {self.name}\n' \
        f'age: {self.age}\n' \
        f'beak: {self.beak}'


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age, "Bubble")
        self.water_type = water_type    
    
    def speak(self):
        print(f"{self.name} says bubble")

    def move(self):
        print(f"{self.name} swims")

    def describe(self):
        print(f"{self.name} is a {self.age} year old fish that lives in {self.water_type}")

    def __str__(self):
        return f'name: {self.name}\n' \
        f'age: {self.age}\n' \
        f'water_type: {self.water_type}'


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age, "meow")
        self.indoor = indoor    
    
    def speak(self):
        print(f"{self.name} says meow")

    def move(self):
        print(f"{self.name} walks")

    def describe(self):
        print(f"{self.name} is a {self.age} year old cat that is an {self.indoor}")

    def __str__(self):
        return f'name: {self.name}\n' \
        f'age: {self.age}\n' \
        f'indoor: {self.indoor}'

"""
class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
       self.__name = name

    def set_phone(self, phone):
       self.__phone = phone

    def set_email(self, email):
       self.__email = email

    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email

    def __str__(self):
        return f'name: {self.__name}\n' \
               f'name: {self.__phone}\n' \
               f'name: {self.__email}'"""