'''
elabore un programa en python 
que determine si usted puede:
a)casarse
b)comprometerse
c)QUEDARSE SOLTERO
con base en las siguientes 
caracteristicas (variable):
- estado civil ( string=
         "soltero", "casado", "comprometido"
- edad(int)
-temperamento (string =
          "buena persona", "mala persona")
-fisico (string= "lindo/a", "feo/a")

'''

estado_civil=input ("ingresa tu estado civil:(soltero/casado/comprometido")
edad = int(input("ingresa tu edad:"))
temperamento = input("ingresa tu temperamento:(buena peersona/mala persona)")
fisico = input ("ingresa el fisico:(lindo/a/feo/a)")
salario = int (input("ingresa tu salario"))

if estado_civil== "casado" or estado_civil == "comprometido":
    print("no puede acercarte a esa persona,por que ya tienes compromiso ")
elif edad < 18:
    print ("no puedes acercarte a esta persona por que no tienes la edad suficinte ")
elif temperamento == "mala persona":
    print ("no puede acercarte a esta persona ;por que te generaria estress")
elif fisico == "feo":
    print ("no puede acercarte a esta persona ;porque no te atrae fisicamente ")
elif salario < 2000000:
    print ("no puedes acercarte a esa persona, por que es pobre")
else:
    print ("no puede acercarte a esta persona ")
print ("FIN DEL PROGRAMA")  
  