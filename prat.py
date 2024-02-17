class Book:
    price=30
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

book2=Book("backend", 23, "herny", 40)
print(book2.author)
print(book2.price)
print(Book.price)

class Animal:
    name="Dog"
    def __init__(self, name, sound, color):
        self.name=name
        self.sound=sound
        self.color=color

animal1=Animal("Goat", "bleat", "brown")
print(animal1.name)
print(Animal.name)
print(animal1.color)
print(animal1.sound)
