print("\n")

print("\n")

class Parrot:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def sing(self, song):

        return f"{self.name} sings {song}"

    def dance(self):

        return f"{self.name} is now dancing"

blu = Parrot("Blu", 10)

print(blu.sing("happy"))

print("\n")

print(blu.dance())

print("\n")

print("\n")