class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# Example:
p = Person("Areeba", 22)
print(p.introduce())
