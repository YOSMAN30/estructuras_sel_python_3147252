'''
if en cascada: 
estructura de control que
permite evalurvarias condiciones es
cascada, es decir, si la porimera condicion no se cumple
se evalua la suiginte y haci sucesivamente 

'''
#Ejemplo 1:
#modificar el rograma de votacion 
#para para que considere la edad de 17
#años

edad = int(input("Ingresar edad: "))

if edad > 18:
    print("Puede votar")
elif edad == 18:
    print("Bienvenido, puedes votar con contraseña")
elif edad == 17:
    print("Puede votar el próximo año")
elif edad >= 10:
    print("tienes registro civil,no pudes ")
elif edad < 17:
    print("no puedes votar aun")

print("Fin del programa")
