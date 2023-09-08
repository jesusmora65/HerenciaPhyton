from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
print("Cuadrado".center(50, "-"))
cuadrado = Cuadrado(4, "Amarillo")
print(f"El área del ciadrado es: {cuadrado.CalcularArea()}")
print(cuadrado)
print("Rectpangulo".center(50, "-"))
rectangulo = Rectangulo(4, 2, "Verde")
print(f"El área del rectángulo es: {rectangulo.CalcularArea()}")
print(rectangulo)