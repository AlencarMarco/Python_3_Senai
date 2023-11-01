class Shape():
    def calcular_area(self):
        pass

class Circulo(Shape):
    def calcular_area(self, r,pi ):    
        return  (r * r * pi)

class Retangulo(Shape):
    def calcular_area(self, b, a):
        return (b * a)
    
circulo = Circulo()
retangulo = Retangulo()

circulo.calcular_area(2,3.14)
retangulo.calcular_area(20, 10)

print("A área do circulo é: ",circulo.calcular_area(2, 3.14))
print("A área do retangulo é: ",retangulo.calcular_area(20,10))

