class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def login(self):
        print(self.name + "logged in!")
    def logout(self):
        print(self.name + "logged out!")
class admin(user):
    def delete_post(self):
        print(self.name + "deleted a post!")
    def ban_user(self):
        print(self.name + "banned a user!")

user1 = user("Ram", "harid@gmail.com")
admin1 = admin("raghu", "raiunu243@gmail.com")

user1.login() #only user can use this things

# admin can use user thing and admin things also
admin1.login()
admin1.ban_user()