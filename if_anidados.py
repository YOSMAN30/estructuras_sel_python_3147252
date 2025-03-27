'''
if anidados osn estructuras 
selectivas que se encuentran 
dentro de otro if 
syntax:
if condition:
    if condition:
       if condition:
          bloque de instr
       else:
           if condition:
           bloque de instr
       else
           bloque de instr
else:
   bloque de instrucciones
'''

#ejemplo 1 
#modificacion de ejercicio de votacion 
#ahora solo pueden votar si es mayor de edad 
#pero si tienen documento.
#mostrar explicaciones en los otros casos
edad = int(input("ingrese su edad: "))
if edad >= 18:
    documento = input("tiene documento? (si/no): ")
    if documento == "si":
        print ("usted puede votar")
    else :
        print("usted no puede votar") 
        print("porque no tiene documento")
else :
    print("usted no piuede votar") 
    print("porque es meor de edad")
              
    

