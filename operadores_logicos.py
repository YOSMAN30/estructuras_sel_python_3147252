'''
 
 operadores logicos 
 
 Aquellos que operan unica mente 
 con valores booleanos (V F)
 Acorde a las tablas de verad 
 '''
 
 #Ejemplo 1: operadores not:
y=not True 
print("el resultado de operar con not es " ,y)

#Ejemplo 2: operador and:
y = False and True 
print("el resultado de operar con and es " ,y)

#ejemplo 3: operador or 
y= False or False 
print ("el resultado de operar con and es" ,y)

'''
gerarquia de predencia de operadores
(logicos inclusive)
1.          ()
2.          **
3.          *,/,%,
4.          +,-
5.          >,<,>=,<=, !=, ==
6.          not
7.          and
8.          or
9.          =
'''
#ejemplo 4:jerarquia de operadores 
y = False and not True or False
print("el resultado de operar con jerarquia de operadores es" ,y)

#ejemplo 5: operadores relacionales y logicos 
y = not 3 > 4 and 4 == 4 or 3 < 2