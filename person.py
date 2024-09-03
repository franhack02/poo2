class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
    
Demi = Person("Demian","Hervé")
print(Demi.name, Demi.lastname)

Bob = Person("Bob","Esponja")
print(Bob.name,Bob.lastname)

Patricio = Person("Patricio","Estrella")
print(Patricio.name,Patricio.lastname)