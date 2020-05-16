a = input("Ingresa el valor de a: ")
b = input("Ingresa el valor de b: ")

#Asi lo haria antes

"""auxa = a;
a = b;
b = auxa;
"""

#Asi se hace con una sola liea de codigo y lo que significa es que en el valor de a se agregue el de b y en el de b se agregue el de a
a, b = b, a

print(f"El valor de a {a}, El valor de b {b}")