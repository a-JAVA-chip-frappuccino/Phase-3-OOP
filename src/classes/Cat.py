# defines class
class Cat():

    # overriding constructor magic method
    def __init__(self, name, color, age = 1):
        self.name = name
        self.color = color
        self.age = age

    # getter
    def get_name(self):
        return self._name
    
    # setter
    def set_name(self, new_name):
        self._name = new_name

    name = property(get_name, set_name) # property function

    # getter
    @property
    def color(self):
        return self._color
    
    # setter
    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print("That's not a valid age!")
        else:
            self._age = new_age

    # instance method
    def meow(self):
        print("Meeeeeooooooowwwwww!")

    def have_a_birthday(self):
        print("Happy Birthday!")
        self.age += 1 # self.age = self.age + 1

    # overriding __str__ magic method to modify printed object
    def __str__(self):
        return f"Name: {self.name}\nColor: {self.color}\nAge: {self.age}"

'''
    SANDBOX ENVIRONMENT
'''

c = Cat("C", "orange")
peanut = Cat("Peanut", "brown", 5)
prenup = Cat("Prenup", "black", 4)

print(c)

print("")

print(peanut)

prenup.age = 3

print(prenup)