class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user1 = user ("Hari", "harid@gmail.com")
user2 = user ("Das","har@gmail.com")

print(user1.email)
print(user2.name)
