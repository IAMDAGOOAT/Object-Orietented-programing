
class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a ",blu.species)
print("Woo is also a ",woo.species)
print("name os the the parrot is",blu.name)

print("Blu is a ",blu.age)
print("Woo is also a ",woo.age)
