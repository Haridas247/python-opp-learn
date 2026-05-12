from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def login(self):
        pass
class normalUser(user):
     def login(self):
         print(self.name + " logged in with email and password!")
class googleUser(user):
    def login(self):
        print(self.name + " logged in with google account!")

user1 =normalUser ("Hari")
user2 = googleUser("das")
user1.login()
user2.login()
