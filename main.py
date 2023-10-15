class animal:
    def __init__(self, Name, Type, Age):
        self.name = Name * 2
        self.type = Type
        self.age = Age


dog = animal('Max', 'dog', 2 )
cat = animal('Tusic', 'cat', 1 )

print(dog.name)
print(dog.type)
print(dog.age)
