#OOP Example

#From the simple critter example, but with dogs
class Dog(object):
    """A virtual Dog"""
    total = 0
    def _init_(self, name):
        print("A new floof approaches!")
        Dog.total += 1 #each new instance adds 1 to the class att' total
        self.name = name #sets the constructor input to an attribute
    def speak(self):
        print("Woof, I am dog.")
    def 

#main
pup = Dog()
pup.speak()
