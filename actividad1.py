motor_encendido = True

temperatura = int(input("cual es la temperatura del motor "))
 
if temperatura > 80:
     motor_encendido = False
     print("la temperatura es demasiado alta, se apagara")
else: 
    print("latemperatura es baja ,el motor sigue encendido")     