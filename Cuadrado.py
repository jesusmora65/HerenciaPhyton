from Color import Color
from Figura import Figura

class Cuadrado(Figura, Color):
    def __init__(self, lado, color):
        Figura.__init__(self, lado, lado)
        Color.__init__(self, color)

    def  CalcularArea(self):
        return self._alto * self._ancho
    
    def __str__(self):
        return f"Figura {Figura.__str__(self)}, Color {Color.__str__(self)}"