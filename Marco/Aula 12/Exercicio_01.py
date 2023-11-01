"""Crie uma classe "animal" com um metodo 'emitir_som'. 
Crie duas subclasses, ' Cachorro' e 'Gato', que sobrescrevam o método 'emitir_som()'
para exibir "au au" e "Miau", Respectivamente. em seguida, crie instancias de ambas as subclasses e chame o metodo 'emitir_som()' nelas"""

class Animal:
    def emitir_som(self):
        pass
 
class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau"
cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())
print(gato.emitir_som())

