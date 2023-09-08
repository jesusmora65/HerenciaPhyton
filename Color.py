class Color:
    def __init__(self, color):
        self._color = color
    
    @property
    def Color(self):
        return self._color
    
    @Color.setter
    def Color(self, color):
        self._color = color

    def __str__(self):
        return F"Color: {self._color}"
    