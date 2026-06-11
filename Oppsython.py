class Student:
    def __init__(self , name ,age, gender):
        self.name = name
        self.age =age
        self.gender = gender
    def __str__(self):
        return f"Student name {self.name}, age {self.age} gender is {self.gender}"
gender = ""
new = Student("kumar", 37, "Mail")
new2 = Student("Ravi", 21 , "Femail")

print(new )
print(new2)



# for oops second torm 

