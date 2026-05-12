class user:
    def __init__(self, name, email):
        self.name = name
        self.email =email
    def login(self):
        print(self.name + "logged in!")
    
    def logout(self):
        print(self.name + "logged out!")
    
    def upload(self):
        print(self.name +"upload photo")

user1 = user("hari","hari@gmail.com")
user2 = user("das","hdsas@gmail.com")

user1.login()
user1.upload()
user2.logout()


# what i learned 
#methods are function inside a class
# def is keyword is used to create a method
# self i always a first parameter