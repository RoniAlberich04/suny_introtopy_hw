class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()



def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None
    
    if num == 0:
        return 1
    
    return num + factorial(num-1)
  
  
  # fact = 1 #short for factorial
   # counter = 1 #how many loops do we have to do
   # while counter <= num:
    #   fact = fact * counter
    #   counter = counter + 1
   # return fact

thehellisthat = 456 % 10
print(thehellisthat)