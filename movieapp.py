from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, hero, price):
        self.title = title
        self.hero = hero
        self.__price = price

    def get_price(self):
        print("Ticket price" + str(self.__price))

    @abstractmethod
    def book(self):
        pass    

class normalUser(Movie):
    def book (self):
        print(self.title + " booked by normal user")
class IMAxUser(Movie):
    def book(self):
        print(self.title + " booked a IMAX user")

movie1 = normalUser("Avenger", "RDJ", 150)
movie2 = IMAxUser("Spiderman", "Tom Holland", 250)

movie1.book()
movie1.get_price()

movie2.book()
movie2.get_price()
# what i learned
#1. ABC is used for abstraction in python
#2. @abstractmethod means child must define a mehtod
#3. Abstrsct class hides- only shows what
#4. complex logic is hidden inside child classes
