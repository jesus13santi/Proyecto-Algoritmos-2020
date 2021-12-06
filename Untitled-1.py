from Usuario import Usuario
#def estadisticas():
#    with open("BaseDeDatos.txt","r") as bd:
#        contador_masculino=0
#        contador_femenino=0
#        usernames=bd.readlines()
#        contador_generos=[]
#        contador_generos.append(usernames)
#        print (contador_generos)
#        for i in contador_generos:
#            print(i)
#            for a in i:
#                
#                if 'Masculino' in a:
#                    contador_masculino+=1
#                elif 'Femenino' in a:
#                    contador_femenino+=1
#                    
#
#        print(contador_masculino)
#        print(contador_femenino)
#       
#            
#     
#estadisticas()
username='jesus'
nombre='nombre'
edad=18
genero='Masculino'

usuario = Usuario(username, nombre, edad, genero,0)
disparos_realizados=5
username='jesus'
with open("BaseDeDatos.txt", "r") as bd:
                
    datos=bd.readlines()
    lista_vacia=[]
    nuevo_valor=0
    lista_vacia.append(datos)
    for i in datos:
        x=i.split(',')
        for a in x:
                usuario = datos[0]
                usuario[4]=disparos_realizados
                for i in range(len(usuario)):
                    if i != len(usuario) -1:
                        nuevo_valor += usuario[i] + ','
                    else:
                        nuevo_valor += usuario[i] + '\n'
                        datos[0] = nuevo_valor
with open("BaseDeDatos.txt", "w") as bd:
                bd.writelines(datos)





#with open("BaseDeDatos.txt", 'r') as bd:
#    datos = bd.readlines()
#    usuario = datos[seleccion - 1][:-1].split(',')
#nuevo_valor = ''
#for i in range(len(usuario)):
#    if i != len(usuario) -1:
#        nuevo_valor += usuario[i] + ','
#    else:
#        nuevo_valor += usuario[i] + '\n'
#datos[seleccion - 1] = nuevo_valor
#with open("BaseDeDatos.txt", "w") as bd:
#usuario[4] = input("Ingrese el nuevo valor:")
#    bd.writelines(datos)
