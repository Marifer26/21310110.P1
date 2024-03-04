import sys

def menu():
     o1=int (input("programas de las tareas \n1.tareas de la 2-9 introducion a python\n2.tareas de la 10-20 listas \n3.tareas de la 21-28 IF \n4.tareas de la 29-33 FOR\n5.tareas de la 34-42\n6.tareas de la 43-51\n7.Salir\n"))

     match o1:

          case 1:
               o1_1=int (input("\n tarea 2-9\n1.variables\n2.strings\n3.concatenar\n4.upper,lower y title\n5.salto de linea y tabulacion\n6.operaciones basicas\n7.exponentes\n8.los floats y el metodo roud\n"))
               match o1_1:
                    case 1:
                         #TAREA 2
                         t2= "hola bienvenido"
                         a2= 20
                         s2= 20
                         st2= a2+s2 
                         print("TAREA 2\n",t2 )
                         print(st2)
                    case 2:
                         #TAREA 3
                         s3= "un dia "
                         a3= 'vi una vaca '
                         b3='vestida de  "uniforme "fuera de un instituto '
                         print("\nTAREA 3\n",s3,a3,b3)
                    case 3:
                         #TAREA 4
                         t4= "marifer"
                         a4= " Estrada"
                         b4= "Rubio"
                         c4= '10'
                         d4= '20'
                         s4=c4+d4
                         suma3= t4+a4+" "+b4
                         print("\nTAREA 4\n",t4+a4+b4)
                         print(suma3)
                         print(t4+" "+a4+" "+b4)
                         print(s4)
                    case 4:
                         #TAREA 5
                         a5="marifer estrada rubio"
                         b5="jose antonio lopez haro".upper()
                         c5="MARIFER estrada Rubio"
                         a5= a5.title()
                         print("\nTAREA 5\n",a5)
                         print(b5)
                         print(c5.lower())
                    case 5:
                         #TAREA 6 
                         print("\nTAREA 6\n lista de tareas: \n\t1.ingeligencia\n\t2.vibraciones\nfin")                    
                    case 6:
                         #TAREA 7 
                         s7=10+20+30+40
                         r7=80-20-4-5
                         m7=30*5*2
                         d7=80/2/2
                         t7= (60+7)-(68*10)/2
                         print("\nTAREA 7\nresultados:\n\tsuma:",s7,"\n\tresta:",r7,"\n\tmultiplicacion:",m7,"\n\tdivicion:",d7,"\n\toperaciones diferentes:",t7)                    
                    case 7:
                         #TAREA 8 
                         s8=2*2*2*2*2*2*2*2*2*2
                         t8=2**10
                         print("\nTAREA 8\n multiplicacion basica:",s8,"\nelevacion:",t8)
                    case 8:
                         #tarea 9
                         a9=24.123456
                         b9=21.2335566
                         s9=a9+b9
                         print("\n TAREA 9\n",round(s9,2))

          case 2:
               o2=int (input("\n tarea 10-20\n1.lista\n2.posiciones negatidas \n3.eliminar con del\n4.eliminar con remove\n5.eliminar con pop \n6.insertar con eppend\n7.insertar con insert\n8.ordenar con sort y sorted\n9.contar elementos con len\n10.tuplas\n11.de tuplas a listas y viceversa"))
               match o2:
                    case 1:
                         #TAREA 10 
                         l10=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         print("\nTAREA 10\nanimal tortuga:",l10[3],"\nanimal perro:",l10[0])
                    case 2:
                         #TAREA 11
                         l11=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         print("\nTAREA 11\nanimal tortuga:",l10[-4],"\nanimal perro:",l10[-7])
                    case 3:
                         #TAREA 12
                         l12=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         del l12[1]
                         del l12[-3]
                         print("\nTAREA 12\nanimales:",l12)
                    case 4:
                         #TAREA 13
                         l13=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         l13.remove("pato")
                         print("\nTAREA 13\nanimales:",l13)
                    case 5:
                         #TAREA 14
                         l14=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         v14=l14.pop(5)
                         a14=l14.pop(0)
                         print("\nTAREA 14\nanimales que faltan:",v14,"y",a14)                    
                    case 6:
                         #TAREA 15
                         l15=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         l15.append("leon")
                         print("\nTAREA 15\nanimales:",l15)                    
                    case 7:
                         #TAREA 16
                         l16=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         l16.insert( 2,"leon")
                         print("\nTAREA 16\nanimales:",l16)
                    case 8:
                         #TAREA 17
                         l17=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         l17.sort(reverse=True)
                         print("\nTAREA 17\nanimales:",l17)
                    case 9:
                         #TAREA 18
                         l18=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         t18=len(l18)
                         print("\nTAREA 18\nanimales:",len(l18),"\nVariable del total ",t18)
                    case 10:
                         #TAREA 19
                         t19=("perro","gato","pato","tortuga","conejo","pez","elefante")
                         n19=(10,20,30,40)
                         print("\nTAREA 19\nanimal:", t19[4],"\noperacion:",n19[1]+n19[3]*n19[2]/n19[0])   
                    case 11:                     
                         #TAREA 20 
                         l20=["perro","gato","pato","tortuga","conejo","pez","elefante"]
                         t20=("perro","gato","pato","tortuga","conejo","pez","elefante")
                         T20=tuple(l20)
                         L20=list(t20)
                         print("\nTAREA 20\ntupla:",T20,"\nlista:",L20,"\ntipo de dato:",type(T20))                                
          case 3 :
               o3=int (input("\n tarea 21-28\n1.IF y comparacion\n2.IF y ELSE\n3.IF,ELIF,ELSE e INPUT\n4.comprobar datos en listas y tuplas\n5.multiplrs condiciones IF \n6.tips para condiciones\n7.while\n8.while con if\n"))
               match o3:
                    case 1:
                         #TAREA 21
                         a21=12
                         b21=23
                         print("\nTAREA 21" )
                         if a21 == b21:
                              print("a21 es igual a b21 ")
                         if a21 < b21 :
                              print("a21 es menor que b21 ")
                         if a21 > b21 :
                              print("a21 es mañor que b21")
                         if a21 != b21 :
                              print("a21 es diferente a b21")
                    case 2:
                         #TAREA 22 
                         a22= "perro"
                         if a22 == "perro":
                              print("\nTAREA 22\nes igual a perro")
                         else:
                              print("no es perro")
                    case 3:
                         #TAREA 23
                         e23=int(input("\nTAREA 23 \n cual es la respuesta a esta suma 4+5\n"))
                         if e23 ==9:
                              print("la respuesta es corecta ")
                         elif e23 <=7 and e23 >=0:
                              print("es incorecta la respuesta")
                         elif e23 >=11 and e23 <= 100:
                              print("es incorecta la respuesta")
                         elif e23 ==10:
                              print("la respúesta estuvo sercas ")
                         elif e23 ==8:
                              print("la respuesta estuvo sercas ")
                         else:
                              print("la respuesta es invalida")
                    case 4:
                         #TAREA 24
                         a24=input("\nTAREA 24\nintrodusca el animal :\n")
                         an24 = ["perro","gato","conejo","pez","lobo","leo"]
                         if a24 in an24:
                              print("si esta en la lista ")
                         else:
                              print("no esta en la lista")
                    case 5:
                         #TAREA 25
                         a25= int(input("\nTAREA 25 \n introduce un numero del 0 al 3\n"))
                         if a25 == 0:
                              print("seleccionaste la opcion 0")
                         if a25 == 1:
                              print("seleccionaste la opcion 1")
                         if a25 == 2:
                              print("seleccionaste la opcion 2")
                         if a25 == 3:
                              print("seleccionaste la opcion 3")                    
                    case 6:
                         #TAREA 26 
                         a26=300
                         b26= 500
                         print('a26 es menor que b26.') if a26 < b26 else print('a26 no es menor que b26')                    
                    case 7:
                         #TAREA 27
                         a27=20
                         while a27 >=0:
                              print("el valor de a27 es :",a27)
                              a27-= 2
                    case 8:
                         #TAREA 28
                              print("\nTAREA 28\n")
                              a28=0
                              while a28 <=20:
                                   a28 += 2
                                   if a28 == 4 or a28 == 8 :
                                        print("se salto el valor ",a28,"de a28")
                                        continue
                                   if a28 == 16:
                                        print("se rompe el buclecuando a28 valia",a28)
                                        break
                                   print(a28)                        
          case 4:
               o4=int (input("\n tarea 29-33\n1.for\n2.for con range\n3.diccionarios de python\n4.diccionario con for \n5.metodos con diccionarios\n"))
               match o4:
                    case 1:
                         #TAREA 29
                         a29 = ["perro","gato","pez","lobo"]
                         print("\nTAREA 29")
                         for B in a29 :
                              print("el animaal es:",B)     
                    case 2:
                         #TAREA 30 
                         print("\nTAREA 30\n")
                         for x in range (7,800,100):
                              print(x)       
                    case 3:
                    #TAREA 31 
                         a31 ={
                              "perro":"cafe con blanco ",
                              "conejo:": "blanco",
                              "gato": "naranja"
                         }
                         print("\nTAREA 31\n",a31)
                         b31 = a31 ["perro"]
                         print("el perro es: ",b31)
                    case 4:
                         #TAREA 32
                         a32 ={
                              "perro":"cafe con blanco ",
                              "conejo:": "blanco",
                              "gato": "naranja"
                         }
                         print("\nTAREA 32\n",a32)
                         a32 ["perro"]="negro"
                         print("el perro es color :",a32["perro"])
                         for c in a32:
                              print(c,"=",a32[c]+".")
                    case 5:
                         #TAREA 33
                         a33 ={
                              "perro":"cafe con blanco ",
                              "conejo": "blanco",
                              "gato": "naranja"
                         }
                         print("\nTAREA 33\nnumeros de elementos:")
                         print(len(a33))
                         del a33["conejo"] 
                         print(a33)
                         a33["pez"]="morado"
                         print(a33)
          case 5:
               o5=int (input("\n tarea de la 34-42\n1.funciones\n2.args\n3.kwargs\n4.clases y objetos\n5.__init__\n6.self\n7.clases vacias \n8.herencia\n9.herencia propiedad de__init__\n"))
               match o5:
                    case 1:
                         #TAREA 34
                         print("\nTAREA 34")
                         def s34(a34,b34):
                              print(a34+b34)
                         s34(40,50)
                         s34(100,200)
                         s34(3000,7000)
                    case 2:
                         #TAREA 35 
                         def a35(*args):
                              print("\nTAREA 35\nanimal en el espacio",args[2])

                         a35("perro","gato","pez")
                         def b35(*args):
                              r35=args[0]+args[3]*args[2]-args[1]
                              print("operacion=",r35)
                         b35(4,7,3,6,3,4)
                    case 3:
                         #TAREA 36
                         def a36(**kwargs):
                              print("\nTAREA 36\n el animal es "+kwargs["b36"])
                         a36(b36="lobo",c36="leon")
                    case 4:
                         #TAREA 37
                         class a37:
                              nombre=""
                              apellidos=""
                              def i37(self):
                                   print("\nTAREA 37\nnombre:",self.nombre,"\napellido:",self.apellidos)
                         b37=a37()
                         b37.nombre="Marifer"
                         b37.apellidos="Estrada Rubio"
                         b37.i37()
                    case 5:
                         #TAREA 38 
                         class a38:
                              print("\nTAREA 38\n")
                              def __init__(self,b38,c38):
                                   self.b38=b38
                                   self.c38=c38
                              def i38(self):
                                   print("nombre:",self.b38,"\napellidos:",self.c38)
                         d38=a38("Marifer","Estrada Rubio")
                         e38=a38("Antonio","Lopez Haro")
                         d38.i38()
                         e38.i38()
                    case 6:
                         #TAREA 39
                         class a39:
                              print("\nTAREA 39\n")
                              def __init__(self,b39,c39):
                                   self.b39=b39
                                   self.c39=c39
                              def i39(self):
                                   print("nombre:",self.b39,"\napellidos:",self.c39)
                         d39=a39("Marifer","Estrada Rubio")
                         e39=a39("Antonio","Lopez Haro")
                         e39.b39="Jose Antonio"
                         d39.i39()
                         e39.i39()
                    case 7:
                         #TAREA 40
                         print("\nTAREA 40\n")
                         class a40:
                              pass
                         a40()
                              
                    case 8 :
                         #TAREA 41
                         class a41:
                              print("\nTAREA 41\n")
                              def __init__(self,b41,c41):
                                   self.b41=b41
                                   self.c41=c41
                              def i41(self):
                                   print("nombre:",self.b41,"\napellidos:",self.c41)
                         d41=a41("Marifer","Estrada Rubio")
                         e41=a41("Antonio","Lopez Haro")
                         e41.b41="Jose Antonio"
                         d41.i41()
                         e41.i41()
                         class p41(a41):
                              print("\nsup clase\n")
                              def __init__(self,u41):
                                   self.u41=u41
                              def l41(self):
                                        print(self.u41)
                         u41=p41("marifer")
                         u41.l41()
                    case 9:
                         #TAREA 42
                         class a42:
                              print("\nTAREA 42\n")
                              def __init__(self,b42,c42):
                                   self.b42=b42
                                   self.c42=c42
                              def i42(self):
                                   print("nombre:",self.b42,"\napellidos:",self.c42)
                         d42=a42("Marifer","Estrada Rubio")
                         d42.i42()
                         class p42(a42):
                              print("\nsup clase\n")
                              def __init__(self,b42,c42,u42):
                                   self.b42=b42
                                   self.c42=c42
                                   self.u42=u42
                              def l42(self):
                                   print("nombre:",self.b42,"\napellidos:",self.c42,"\nedad",self.u42)
                         e42=p42("Antonio","Lopez Haro","20")
                         e42.l42()
          case 6:
               o6=int (input("\n tarea de la 43-51\n1.variable globales\n2.lambda\n3.fecha\n4.strftime\n5.search\n6.findall\n7.split y sub\n8.secuencias especiales\n9.excepciones\n"))
               match o6:
                    case 1:
                         #TAREA 43
                         def a43():
                              global b43
                              b43=26
                         a43()
                         print("\nTAREA 43\n",b43)
                    case 2:
                         #tarea 44
                         print("\nTAREA 44\n")
                         import math
                         a44=lambda radio:(math.pi*radio*radio)
                         print(a44(5))
                    case 3:
                         #TAREA 45
                         print("\nTAREA 44\n")
                         import datetime
                         a45=datetime.datetime(2003,3,26,5,45,24)
                         print(a45)
                    case 4:
                         #TAREA 46
                         print("\nTRAREA 46\n")
                         import datetime
                         a46 = datetime.datetime.now()
                         print(a46.strftime("fecha de hoy :%x"))
                    case 5 :
                         #TAREA 47
                         print("\nTAREA 47\n")
                         import re
                         a47="Hola mi nombre es Marifer"
                         b47=re.search("Marifer",a47)
                         print(b47)
                    case 6:
                         #TAREA 48
                         print("\nTAREA 48\n")
                         import re 
                         a48="un maestro de todas las areas es un maestro en ni una pero sigue siendo mejor que un maestro es una area "  
                         b48=re.findall("maestro",a48)
                         print(b48)
                    case 7:
                         #TAREA 49
                         print("\nTAREA 49\n")
                         import re 
                         a49="un maestro de todas las areas es un maestro en ni una pero sigue siendo mejor que un maestro es una area "  
                         b49=re.split("maestro",a49,)
                         c49=re.sub(" ","-",a49,9)
                         print(c49)
                         print(b49)
                    case 8:
                         #TAREA 50
                         print("\nTAREA 48\n")
                         import re 
                         a50="un maestro de todas las areas es un maestro en ni una pero sigue siendo mejor que un maestro es una area "  
                         b50=re.findall("[a-e]",a50)
                         print(b50)
                    case 9:
                         #TAREA 51
                         b51="declarada"
                         try:
                              print(b51)
                         except:
                              print("no esta declarada ")
                         try:
                              print(a51)#variable no declarada para la practica de variable no declarada 
                         except:
                              print("no esta declarada")                   
          case 7:
               sys.exit()
while(1):
     menu()
