#Exercise taken from techgeekbuzz.com

# Python OOPs Exercise 1: Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.

class Students:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

becky = Students('Becky', 12 , '6th')    

#Python OOPs Exercise 2: Write a Program to create an empty valid class by name Students, with no properties

class Students:
  pass

rose = Students()

#Python OOPs Exercise 3: Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff
class Staff:
  def __init__(self, role, dept, salary):
    self.role = role
    self.dept = dept
    self.salary = salary
    
  def show_details(self):
    print('Name:  ', self.name)  
    print("Age: ", self.age)
    print("Role:", self.role)
    print("Department:", self.dept)


class Teacher(Staff):
  def __init__(self, name, age):
        self.name = name
        self.age = age
        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)
        
teacher = Teacher("Raj", 28)

#access the Staff Method
teacher.show_details()        