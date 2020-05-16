#Importamos la libreria del math
import math



pi = math.pi
radio = float(input("Ingresa el valor del radio del Circunferencia: "))
area = pi * radio**2
longitud = 2 * pi * radio

"""Para agregar un cierto numero de decimales se poe el dos puntos, punto, numeros que deben de aparecer"""
print(f"E valor del area es {area:.4f}")
print(f"El valor del perímetro es {longitud:.4f}")
