class user:
    def __init__(self, name, password):
        self.name       = name
        self.__password =password 
        # __ it mean hidden\private
    def check_password(self, entered_password):
        if entered_password == self.__password:
            print("password correct! Welcome" + self.name)
        else:
            print("wrong password")

user1 =user("hari", "hari246#")
user2 =user("kavi","kavi9845#!")

user1.check_password("hari246#")

print(user1.__password)