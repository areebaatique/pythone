class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Example:
s = Student("Areeba")
s.add_grade(80)
s.add_grade(90)
print(f"{s.name}'s average grade is: {s.average()}")

