
n_talentos=[]
talentos=[]
nota=[]
t_final=[]

menu=int(input("menu \n 1.cuantos talentos desea ingresar.\n 2.dijite el nombre del talento y el codigo.\n 3.dijite la nota del talento en la mision 1.\n 4.dijite la nota del talento en la mision 2.\n 5.dijite la nota del talento en la mision 3.\n 6.dijite la nota del talento en la prueba final.\n 7.mostrar el nombre y codigo del talento con mejor nota en la mision 1.\n 8.mostrar el nombre y codigo del con mejor nota en la mision 2.\n 9.mostrar el nombre y codigo del con mejor nota en la mision 3.\n 10.mostrar el nombre y el promedio de cada talento.\n 11.mostrar todos los datos del talento.\n 12.nonbre del autor.\n 13.salir.\n"))

while menu!=13:
    
    if menu==1:
        n_talentos=int(input("cuantos talentos desea ingresar"))
    
    elif menu==2:
        for i in range(n_talentos):
            talentos=nombre=(input("nombre del talento"))
            talentos=codigo=int(input("dijite el codigo del talento"))
    elif menu==3:
        for i in range(n_talentos):
            nota=Mision1=int(input("dijite la nota del talento en la mision 1"))
            while nota >0 or  nota<=100:
                Mision1=[]
            else:
                print("nota invalida")
                nota=Mision1=int(input("dijite la nota del talento en la mision 1"))
    elif menu==4:
        for i in range(n_talentos):
            nota=Mision2=int(input("dijite la nota del talento en la mision 2"))
            while nota >0 or  nota<=100:
                Mision2=[]
            else:
                print("nota invalida")
                nota=Mision2=int(input("dijite la nota del talento en la mision 2"))
    elif menu==5:
        for i in range(n_talentos):    
            nota=Mision3=int(input("dijite la nota del talento en la mision 3"))
            while nota >0 or  nota<=100:
                Mision3=[]
            else:
                print("nota invalida")
                nota=Mision3=int(input("dijite la nota del talento en la mision 3"))
    elif menu==6:
        for i in range(n_talentos):    
            nota=t_final=int(input("dijite la nota del talento en la evaluacion final"))
            while nota >0 or  nota<=100:
                t_final=[]
            else:
                print("nota invalida")
                nota=t_final=int(input("dijite la nota del talento en la evaluacion final"))
    elif menu==7: 
        for i in range(n_talentos):
            def mayor(Mision1):
                max = Mision1[0];
                for x in Mision1:
                    if x > max:
                        max = x
                return max
    elif menu==8:
        for i in range(n_talentos):
            def mayor(Mision2):
                max = Mision2[0];
                for x in Mision2:
                    if x > max:
                        max = x
                return max
    elif menu==9:
        for i in range(n_talentos):
            def mayor(Mision3):
                max = Mision3[0];
                for x in Mision3:
                    if x > max:
                        max = x
                return max
    elif menu==10:
        for i in range(n_talentos):
            nota=(Mision1+Mision2+Mision3+t_final)/4
            print(nota)
    elif menu==11:
        print (talentos)
        print(Mision1)
        print(Mision2)
        print(Mision3)
        print (nota)
        print(t_final)
    elif menu==12:
        print("el nombre del autor de este programa es johan sebastian sarmiento chaves")
    elif menu==13:
        print("chao")
    else:
        print("valio mondongo")
    menu=int(input("menu \n 1.cuantos talentos desea ingresar.\n 2.dijite el nombre del talento y el codigo.\n 3.jitite la nota del talento en la mision 1.\n4.dijite la nota del talento en la mision 2.\n 5.dijite la nota del talento en la mision 3.\n6.dijite la nota del talento en la prueba final.\n7.mostrar el nombre y codigo del con mejor nota en la mision 1.\n8.mostrar el nombre y codigo del con mejor nota en la mision 2.\n9.mostrar el nombre y codigo del con mejor nota en la mision 3.\n10.mostrar el nombre y el promedio de cada talento.\n11.mostrar todos los datos del talento.\n12.nonbre del autor.\n13.salir.\n"))



