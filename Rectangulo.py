from Color import Color
from Figura import Figura

class Rectangulo(Figura, Color):
    def __init__(self, ancho, alto, color):
        Figura.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def  CalcularArea(self):
        return self._alto * self._ancho
    
    def __str__(self):
        return f"Figura {Figura.__str__(self)}, Color {Color.__str__(self)}"