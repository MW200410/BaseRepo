class Person():
    def __init__(self, firstname, lastname):  # Added params to the contructor
        self._firstname = firstname
        self._lastname = lastname

    def print(self): 
        print(self._firstname + " -- " + self._lastname)  # underscores indicate that these attributes/properties are private


    @property # Decorator 
    def firstName(self):
        print("In GET METHOD")
        return self._firstname
    
    @firstName.setter
    def firstName(self, newfirstName):
        print("In SET METHOD")
        self._firstname = newfirstName
