class Dog:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      
buster = Dog('Buster', '15')
magic = Dog('Magic','7' )

print(Dog('Buster', '15'))
print(Dog('Magic','7'))

print(buster)
print(buster.name, buster.age)
