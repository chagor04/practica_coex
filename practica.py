
#primer ejercicio basico
#escribir hola mundo en pantalla
#print["hola mundo"]

#segundo ejercicio basico
#almacenar hola mundo en una cadena y mostrarla despues 
#hola=["hola mundo"]
#print (hola)

#tercer ejercicio basico
# preguntar el nombre el usuario y despues saludar con el nombre 
#nombre = input("dijite su nombre:")
#print ("hola"+nombre)

#se desea llenar una lista con 10 animales, y le han pedido a usted que sabe programar
#que les ayude para solicitar esos 10 nombres, mostrarlos ordenados alfabeticamente,
#luego solicitar al usuario un numero entre el 1 y el 10 y que le permita ver cuales
#animales se encuentran en el numero dicho y el final de la lista .Tambien cree una opcion que permita al usuario escribir el nombre de un animal y verificar si ese animal se encuentra en la lista.

#animales=[]
#list=[]

#animales=input("digite los animales que decees hacer la lista")
#animales.sort()

#list=input()

#
#lista= [1,0,4,8,5,7,6,8,7,5,6,4,3,1,9,2]
#salir= False

#cont =input ('dijite el numero q desee encontrar en la lista')
#lista.index(cont)

#lista.count(cont)

#sumar los valores del siguiente arreglo numeros= 33,55,77,81,48 mostrar al final del programa los 
#los numeros en forma de lista y el resultado de la suma 
#from ast import Num

#numeros=[33,55,77,81,48]
#numeros.sort

#for i in numeros:
#    print(i)
#print("total:",sum(numeros))

#numeros=0
#como se utiliza la funcion max y min
#lista=[1,2,3]
#lista2=["a","b","z"]
#print(max(lista))
#print(min(lista2))

#se utiliza la funcion divmod
#print(divmod(25,45))
#a,b=print(divmod(2,4))
#print(a)

#from mailbox import NoSuchMailboxError
#estudi=(int(input("cuantos estudiantes va a dijitar")))

#nombre=[]
#nom={}
#cursoestudiantes=[]

#for i in range(estudi):
#    nom["nombre"]=input("sigite el nombre")
 #   nom["curso"]=int(input("diga su curso"))
 #   nom["genero"]=input("genero")
 #   nombre.append(nom)
#    nom=[]


#for i in range(estudi):
#    nombre.append(input("digame su nombre"))
#    curso=(int(input("de que curso eres")))
#    while curso <1 or curso >11:
#        print("curso invalido")
#        curso=(int(input("de que curso eres")))
#    else:
#        cursoestudiantes.append()
#   
 #   genero=(input("cual es tu genero"))
#notas=(int(input("cuales son sus notas ")))
#if notas:
#    notas>=3.5 
#    print("usted esta aprobado")
#else:
 #   notas<3.5
  #  print("usted esta desaprobado")



#N_trabajadores=(int(input("cuantos trabajadores quiere ingresar: ")))
#trabajadores=[]
#trabajador={}

#for i in range(N_trabajadores):
#    trabajador["nombre",i]=input("digite el nombre el trabajador: ")
#    a=(int(input("dijite cuantos años tiene en la empresa: ")))
#    trabajador["antiguedad",i]= a
#    b=(int(input("dijite las horas trabajadas en el mes: ")))
#    trabajador["H_trabajadas",i]=b
#    c=(int(input("cuanto cobras por hora: ")))
#    trabajador["V_hora",i]=c
#    d=(c*b+(a*30))/13
#    trabajador["sueldo",i]=d
#print(trabajador)




N_estudiantes=(int(input("cuantos estudiantes desea ingresar")))
estudiantes=[]
alumnos={}

for i in range(N_estudiantes):
  alumnos["nombre",i]=input("escriba el nombre del alumno: ")
  alumnos["codigo",i]=(int(input("escriba el codigo del estudiante: ")))
  alumnos["promedio",i]=(int(input("escriba el promedio de los alumno: ")))


print("------------------MENU------------------")
print("1. saber cuantos aprobaron la materia")
print("2. saber cuantos habilitan en diciembre")
print("3. saber cuantos habilitan en marzo")
print("4. saber quien saco el mejor promedio")
print("5. salir")
print("-----------------------------------------")

menu=int(input("introduzca su opcion "))

while menu!=5:
  if menu==1:
    for i in range(N_estudiantes):
      alumnos("promedio")>0 or alumnos("promedio") <=100
      