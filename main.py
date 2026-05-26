from animals import Animal, Dog, Bird, Fish, Cat

def main():
    # Create one instance of each animal subclass
    animals = [
        Dog("Jeff", "12", "Golden Retriever"),
        Bird("Mark","10","long Beak"),
        Fish("Dave", "4", "fresh Water"),
        Cat("Maisie", "5", "indoor cat")
    ]

    # TODO: instantiate your animals and add them to the list

    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        animal.speak()
        animal.move()
        animal.describe()
        print()


if __name__ == "__main__":
    main()
