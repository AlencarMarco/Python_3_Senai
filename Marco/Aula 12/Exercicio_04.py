class Animal():
    def mover(self):
        pass

class Peixe(Animal):
    def mover(self):
        return "Nadando"
    
class Ave(Animal):
    def mover(self):
        return "Voando"
    
ave = Ave()
peixe = Peixe()

print(peixe.mover())
print(ave.mover()) 