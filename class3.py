print("\n")

print("\n")

class Parrot:

    species = "bird"

    def __init__(self, name, age):

        self.name = name

        self.age = age

blu = Parrot("Blu", 10)

woo = Parrot("Woo", 15)

print(f"Blu is a {blu.species}")

print("\n")

print(f"Woo is also a {woo.species}")

print("\n")

print(f"{blu.name} is {blu.age} years old")

print("\n")

print(f"{woo.name} is {woo.age} years old")

print("\n")

print("\n")