import os
import time
import csv


# PROGRAMA DE VALIDACION DE USUARIOS
## MODIFICACION GITHUB
#Jaime DelgadillO lOPEZ


Diccionario={}   # Creamos un diccionario vacio
principal=True
registro=True
ini=True
while principal==True:   #Mientras la variable "principal" sea = True, entonces:
        os.system("cls")
        try:
            menu=int(input("[1]....Inicio de sesion\n[2]....Registrar usuario\n[3]....Eliminar usuario\n[4]....Guardar usuarios en un archivo .csv\n[5]....Salir\nElija Opcion : ")) 
        except ValueError:
            print ("Opcion no valida")
            time.sleep(2)
            continue
           
        if menu==1:                                   #si el valor de la variable "menu" = 1, entonces:
            ini=True
            while ini==True:     
                os.system("cls")
                user=input("Ingrese Usuario : ")      #Lo que ingrese el usuario, sera asignado a la variable "user"   
                if Diccionario.get (user):            #Si dentro del {Diccionario} de encuentra el valor de la variable "user", entonces:
                    p=Diccionario[user]               ##Se asigna el valor de la variable "user" encontrada en el {Diccionario} la variable "p"  
                    passw=int(input("Ingrese Contraseña :"))
                    if passw == p:                    #Si la variable "passw" ingresada coincide con la contraseña almacenada en el {Diccionario}:
                        print("Acceso concedido ")
                        time.sleep(2)
                        break
                    else:
                        print ("Acceso denegado ") 
                        time.sleep(2)   
                        denuevo=(input("Desea intentar nuevamente S/N : "))
                        if denuevo=="S" or denuevo=="s":
                            os.system("cls")
                            continue
                        else:
                            break
                else:
                    print("Usuario incorrecto o no existe")
                    nueva=(input("Quiere intentar nuevamente S/N : "))
                    if nueva=="S" or nueva=="s":
                        user=""
                        passw=0
                        continue
                    else:
                        user=""
                        passw=0
                        break

        elif menu==2:                                           #Si el valor de la variable "menu" = 2, entonces:
            registro=True
            while registro ==True:          
                user=(input("Ingrese Usuario : "))
                try:
                    passw=int(input("Ingrese clave numerica : "))
                except ValueError:
                    print ("La contraseña debe tener un valor numerico ")
                    time.sleep(2)
                    continue     
                
                Diccionario[user]=passw                         # Agrega al {Diccionario} la pareja clave-valor, donde keys() es el usuario y el values() es la contraseña
                print(Diccionario)
                otra=(input("Desea agregar otro usuario S/N :"))
                if otra=="S" or otra=="s":
                    os.system("cls")
                    continue
                elif otra != 1:
                    os.system("cls")
                    registro=False
          
        elif menu==3:                                           #Si el valor de la variable "menu" = 3, entonces:
            print("Eliminar usuario")
            claves = list(Diccionario.keys())                   #Se le asigna a la variable "claves", el listado de solo los valores de keys()
            print ("─"*100)
            print(claves)                                       #Se imprime solo los valores de keys()
            print("─"*100)
            borrar=input("¿Que usuario quiere borrar? : ")
            if Diccionario.get (borrar):                        #Si dentro de {Diccionario} se encuentra el valor de variable "borrar"
               print ("existe")
               password = Diccionario[borrar]                   #Se asigna el valor de la variable "borrar" encontrada en el {Diccionario} la variable "password" 
               contra=int(input("Para eliminar usuario, ingrese contraseña : "))      
               if contra == password:                           #Si el valor de la variable "contra" es = a la variable "password", entonces   
                   print("contraseña es correcta")
                   time.sleep(2)
                   del(Diccionario[borrar])                     #Borra del {Diccionario} el valor de la variable "borrar" ingresada por usuario
               else:
                   print("Contraseña incorrecta ")
                   time.sleep(2)
            else:
                print("El valor no existe")
                time.sleep(2)
                continue   
        
        elif menu==4:
            with open("Usuarioycontraseña.csv","w") as userpass:   #Se crea un archivo .csv, con permiso de escritura y le damos un alias
                escritor=csv.writer(userpass)                      #Creamos un objeto escritor de CSV asociado al archivo. 
                for x,y in Diccionario.items():                    #Recorremos sobre cada clave y valor en el {diccionario}"x"=primer valor de keys() e "y"=primer valor de values() 
                    escritor.writerow([x,y])                       #Escribimos una fila en el archivo CSV con la clave y el valor. 
                   
        elif menu==5:
            principal=False
        
        elif menu<1 or menu>4:
            print("opcion no valida ")
            time.sleep(2)
            continue
      