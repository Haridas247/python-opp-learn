class user:
    app_name = "StarApp"

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
user1 = user("Hari", 22, "harid3837@gmail.com")
user2 = user("das",24, "hdas9523@gmail.com")
# intance varible to print
print(user1.name)
print(user2.age)

# class variable to print
print(user1.app_name)
print(user1.app_name)


