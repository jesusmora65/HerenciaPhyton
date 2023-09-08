from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def Ancho(self):
        return self._ancho
    
    @Ancho.setter
    def Ancho(self, ancho):
        self._ancho = ancho

    @property
    def Alto(self):
        return self._alto
    
    @Alto.setter
    def Alto(self, alto):
        self._alto = alto
    
    @abstractmethod
    def CakcularArea(self):
        pass

    def __str__(self):
        return f"Figura: Ancho = {self._ancho}, alto = {self._alto}"
