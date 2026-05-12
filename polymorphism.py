class User:
    def __init__(self, name):
        self.name = name
    
    def send(self):
        print(self.name + "sent a message!")
    
class Admin(User):

    def send(self):
        print(self.name + "send a warning message")
class Support(User):
    def send(self):
         print(self.name + "send a ticket reply")

user1 = User("hari")
admin1 = Admin("das")
support1 = Support("kavi")

user1.send()
admin1.send()
support1.send()