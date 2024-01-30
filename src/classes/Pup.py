class Pup():

    def __init__(self, name, isGoodBoy = True):
        self.name = name
        self.isGoodBoy = isGoodBoy

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name) > 2:
            self._name = new_name
        else:
            raise Exception("Name must be a string and longer than 2 characters!") # raises specific error
        
    @property
    def isGoodBoy(self):
        return self._isGoodBoy
    
    @isGoodBoy.setter
    def isGoodBoy(self, new_isGoodBoy):
        # if new_isGoodBoy == True or new_isGoodBoy == False:
        if type(new_isGoodBoy) == bool:
            self._isGoodBoy = new_isGoodBoy
        else:
            raise Exception("isGoodBoy must be a Boolean value!")
        
    def make_a_collar(self):
        print(f"You have a new collar with {self.name}")

'''
    SANDBOX ENVIRONMENT
'''

warbertun = Pup("Warbertun", True)
patrick = Pup("Patrick", isGoodBoy = False)

warbertun.make_a_collar()
patrick.make_a_collar()