from random import randint
from Usuario import Usuario
from Barcos import Barco
#tamanio=Barco(tamanio)
#orientacion=Barco(orientacion)
#locacion=Barco(locacion)
def main():
    
    '''Funcion Principal'''    
    print('''
Bienvenidos al juego de batalla naval
    ''')
    '''Comienzo del programa'''
    '''Ciclo repetitivo para que el juego no se detenga.'''
    while True:
        usuarios=[]
        '''Valida que le usuario coloque una opcion correcta'''
        comienzo_juego=input('''
-------------------        
1-Nuevo juego 
2-Modificar usuario
3-Salir
-------------------
        ''')
        print('-'*19)
        if comienzo_juego== '1':
            while True:
                '''Valida que se debe crear nuevo usuario'''
                validacion_usuario=input('''
1-Nuevo Usuario
2-Usuario existente
-------------------
            ''')
                print('-'*20)
                if validacion_usuario=='1':
                    print('''
-----------------------------------------------------------
Para ingresar el usuario debe tener en cuenta lo siguiente:
    -Debe ser escrito todo en minusculas.
    -NO debe contener minusculas.
    -No debe sobrepasar los 30 caracteres.
-----------------------------------------------------------
                ''')

                    '''Llama la funcion usuario()'''
                    usuario()
                     
                    print('-'*20)
                elif validacion_usuario=='2':
                    '''Valida que el usuario ya existe'''
                    while True:
                        '''Valida que se ingrese un usuario ya existente'''
                        usuarios=input('ingrese su usuario: ')
                        if verificar_username_existe(usuarios):
                            print('Usuario Verificado.')
                            break
                        else:
                            print('El usuario no existe. Porfavor ingresa un usario existente')
                    break
                else:
                    print('Ingrese una opcion valida.')
            '''Comienza el juego'''
            print('Comienzo de Juego')
            comenzar_juego()
            
            

           
        elif comienzo_juego=='2':
            print('''
        ¿Que desea hacer?
        1-Editar Usuario
        2-Eliminar Usuario
        3-Ver Usuarios
            
''')
            opcion=int(input('Ingrese una opcion: '))
            if opcion==1:
                '''Edita el usuario'''
                ver(edit = True)
                seleccion = int(input("Seleccione el usuario que desee actualizar: "))
                actualizar(seleccion)
                print('Usuario Editado Correctamente')
            elif opcion==2:
                '''Elimina el usuario que el usuario desee'''
                ver()
                seleccion = int(input("Seleccione el usuario que desee eliminar: "))
                eliminar(seleccion)
                print('Usuario Eliminado Correctamente')
            elif opcion==3:
                '''Ve todos los usuarios'''
                ver()
        elif comienzo_juego=='3':
            print('Gracias por visitar nuestro juego.\nTe esperamos pronto.')
            break
        else:
        
            print('Ingrese una opcion valida')





def verificar_username_existe(username):
    '''Funcion para verificar si el usuario existe'''
    try:
        all_users = open('BaseDeDatos.txt', 'r').readlines()# Otra forma de acceder a un archivo
        for user in all_users:
            usuario = user[:-1].split(',') # [:-1] para quitar el salto de linea
            if usuario[0] == username:
                return True
        return False
    except FileNotFoundError:
        print('Todavia no se ha registrado ningun usuario')
        return False
def buscar_usuario(username):
    '''Funcion para buscar un usuario'''
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        if usuario[0] == username:
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])

def usuario():
    '''Funcion para ingresar un nuevo usuario'''
    contador=0
    validez=True
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros= ['1','2','3','4','5','6','7','8','9','0','']
    validez2=False
    

    while validez== True:
        contador=0 
    
        username= input('Usuario: ')
        
        for i in username:
            '''Valida que el usuario no contenga espacios o mayusculas'''
            if i==' ':
                contador+=1
            if i in mayusculas:
                contador+=1
        
        if len(username) > 30:
            '''Valida que el usuario no contenga mas de 30 caracteres'''
            contador+=1
       
                
        if contador>=1:
            print('Usuario Incorrecto.\nPorfavor verifique que el usuario contenga menos de 30 caracteres, no contenga mayusculas ni espacios.')
            print('-'*30)
        elif verificar_username_existe(username):
            '''Valida que el usuario que se ingresa no se repita'''
            print('Usuario Existente.\nPor favor ingrese otro usuario')
                
            
        elif username=='':
            '''Valida que el usuario no de enter sin ningun caracter'''
            print('Ingresa algun caracter')
            print('-'*93)
        elif len(username)<=3:
            print('Ingrese mas de 3 caracteres')

            
        else:
            validez=False      
            validez2=True 
        
        
    print('-'*19)
    while validez2==True:
        contador=0
        nombre=input('Nombre Completo: ')
        for i in nombre:
            if i in numeros:
                contador+=1
        if contador>=1:
            print('No ingrese numeros. Ingrese solo letras.\nVuelve a intentarlo')
            print('-'*19)
        else:
            '''Coloca la primera letra de cada nombre o apellido en un mayuscula'''
            nombre=nombre.title()
            validez2=False
    print(nombre)
    
    
    print('-'*19)
    while True:
        '''Valida que la edad este ente 5 y 100 años, y que sea solo caracter numerico'''
        try:
            edad=int(input('Edad: '))
            while edad<=5 or edad>=100 :
                print ('Edad incorrecta. \nverifique que este ingresando una edad valida.')
                print('-'*19)
                edad=int(input('Edad: '))
            break
        except ValueError:
            print('Edad Incorrecta.\nPor favor ingrese un numero')
            print('-'*19)
               
                    
                
    print('-'*19)            
    while True:
        '''Valida que solo ingrese m o f'''
        genero=input('Genero (Masculino(M) , Femenino(F)): ')
        genero.lower
        if genero=='m':
            genero='Masculino'
            print(genero)
            break
        elif genero =='f':
            genero='Femenino'
            print(genero)
            break
        else:
            if genero=='':
                '''Valida que no haga enter sin escribir nada'''
                print('No deje espacio en blanco')
            else:
                print('Ingrese una letra valida (m o f)')
                print('-'*93)
    usuario = Usuario(username, nombre, edad, genero)
    '''Agrega el usuario insertado en la Base de Datos'''
    with open("BaseDeDatos.txt", "a+") as bd: #El a+ es por si el archivo no se ha creado entonces se crea
        bd.write("{},{},{},{}\n".format(username, nombre, edad, genero))
    print('\tUsuario: ', usuario.username, ' registrado correctamente')
    return Usuario
def ver(edit = False):

    '''
    Funcion para ver los usuarios en la base de datos
    '''
    print(
        '''
        Estos son los usuarios registrados actualmente:
        '''
    )
    usuarios = []
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
        #print(i+1, " - Estudiante {} de {} años, titular de la cedula {} y el carnet {} estudia {}".format(estudiante.nombre, estudiante.edad, estudiante[1], estudiante[2], estudiante[3]))
    #usuarios = sorted(usuarios, key= lambda user: user.username)
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for i, user in enumerate(usuarios):
        print('-'*5, i+1, '-'*5)
        print(user)
def actualizar(seleccion):
    '''
    Funcion que permite actualizar atributos de los usuarios registrados en la base de datos
    '''
    print('''
    ¿Qué atributo desea modificar?
    1 - Username
    2 - Nombre
    3 - Edad
    4 - Género
    ''')
    selec  = int(input('''
    Seleccione una opción
    '''))

    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()
        usuario = datos[seleccion - 1][:-1].split(',')
    usuario[selec - 1] = input("Ingrese el nuevo valor:")
    nuevo_valor = ''
    for i in range(len(usuario)):
        if i != len(usuario) -1:
            nuevo_valor += usuario[i] + ','
        else:
            nuevo_valor += usuario[i] + '\n'
    datos[seleccion - 1] = nuevo_valor
    with open("BaseDeDatos.txt", "w") as bd:
        bd.writelines(datos)
def eliminar(seleccion):
    '''
    Funcion para eliminar un usuario de la base de datos
    '''
    with open("BaseDeDatos.txt", "r") as bd:
        lines = bd.readlines()
        suprimir = lines[seleccion - 1]
    with open("BaseDeDatos.txt", "w") as bd:
        for line in lines:
            if line != suprimir:
                bd.write(line)

def comenzar_juego():
    fila=10
    columna=10
    oceano=[]
    tablero=[]
    for i in range(10):
        '''Crea dos tableros'''
        '''Matriz falsa''' 
        tablero.append(["O"]*10)
        '''Matriz de juego'''
        oceano.append(['O']*10)



    def ubicaciones_disponibles(tamanio, orientacion):
        locacion = []

        if orientacion != 'horizontal' and orientacion != 'vertical':
            raise ValueError("Orientation must have a value of either 'horizontal' or   'vertical'.")

        if orientacion == 'horizontal':
            fila_random = randint(0, fila-1)
            columna_random = randint(0, columna - tamanio + 1)
        elif orientacion == 'vertical':
            fila_random = randint(0, fila - tamanio + 1)
            columna_random = randint(0, columna-1)

        if orientacion == 'horizontal':
            if columna_random + tamanio <= columna and ('P' not in tablero[fila_random] [columna_random:columna_random+tamanio]):
                locacion = {'fila': fila_random, 'col': columna_random}
        elif orientacion == 'vertical':
            if fila_random+tamanio <= fila and 'P' not in [tablero[i][columna_random] for i in  range(fila_random, fila_random+tamanio)]:
                locacion = {'fila': fila_random, 'col': columna_random}
            

      # Aca veo los bordes finales
        if locacion:
            if orientacion == 'horizontal':
                if (columna_random-1 >= 0 and columna_random+tamanio+1 < columna and ('P' !=    tablero[fila_random][columna_random+tamanio+1]) and ('P' != tablero    [fila_random][columna_random-1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 >= 0 and columna_random+tamanio+1 >= columna and ('P'    != tablero[fila_random][columna_random-1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random+tamanio+1 < columna and columna_random-1 < 0 and ('P' !=   tablero[fila_random][columna_random+tamanio+1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []

            elif orientacion == 'vertical':
                if (fila_random-1 >= 0 and fila_random+tamanio+1 < fila and ('P' != tablero [fila_random-1][columna_random]) and ('P' != tablero[fila_random+tamanio+1]  [columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 < 0 and fila_random+tamanio+1 < fila and ('P' != tablero    [fila_random+tamanio+1][columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 >= 0 and fila_random+tamanio+1 >= fila and ('P' != tablero  [fila_random-1][columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []

      #Aca veo los bordes laterales
        if locacion:
            if orientacion == 'horizontal':
                if (fila_random-1 >= 0 and fila_random+1 < fila and ('P' not in tablero [fila_random+1][columna_random:columna_random+tamanio]) and ('P' not in tablero  [fila_random-1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 < 0 and fila_random+1 < fila and ('P' not in tablero    [fila_random+1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 >= 0 and fila_random+1 >= fila and ('P' not in tablero  [fila_random-1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []
            if orientacion == 'vertical':
                if (columna_random-1 >= 0 and columna_random+1 < columna and ('P' not in    [tablero[i][columna_random-1] for i in range(fila_random, fila_random+tamanio)]     and 'P' not in [tablero[i][columna_random+1] for i in range(fila_random,   fila_random+tamanio)])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 < 0 and columna_random+1 < columna and ('P' not in   [tablero[i][columna_random+1] for i in range(fila_random, fila_random+tamanio)]   )):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 >= 0 and columna_random+1 >= columna and ('P' not in     [tablero[i][columna_random-1] for i in range(fila_random, fila_random+tamanio)] )):
                    locacion = {'fila': fila_random, 'col': columna_random}
            else:
                locacion = []
        

        if not locacion:
            return 'None'
        else:
            return locacion


    def selecciona_ubicacion(tamanio):
        orientacion = 'horizontal' if randint(0, 1) == 0 else 'vertical'
        locacion = ubicaciones_disponibles(tamanio, orientacion)
        
        print(locacion)
        if locacion == 'None':
            return 'None'
        else:
            return {'locacion': locacion, 'tamanio': tamanio, 'orientacion': orientacion}
       
    


    def print_tablero(tablero):
        print("\n  " + " ".join(str(x) for x in range(0, columna )))
        for r in range(fila):
            print(str(r) + " " + " ".join(str(c) for c in tablero[r]))
        print()


    # creo 3 de 3 casillas
    temp = 0
    while temp < 1:
        barco_info = selecciona_ubicacion(3)
        if barco_info == 'None':
            continue
        else:
            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).fillBoard(fila,columna,tablero)
            
            temp += 1
    del temp

    # creo 3 de 2 casillas
    temp = 0
    while temp < 1:
        barco_info = selecciona_ubicacion(2)
        if barco_info == 'None':
            continue
        else:
            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).fillBoard(fila,columna,tablero)
            
            temp += 1
    del temp


    # creo 3 de 1 casilla
    temp = 0
    while temp < 4:
        barco_info = selecciona_ubicacion(1)
        if barco_info == 'None':
            continue
        else:
            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).fillBoard(fila,columna,tablero)
            
            temp += 1
    del temp





    

    print_tablero(tablero)
    print('-'*10)
    print_tablero(oceano)

    def juego(oceano,tablero):
        hundir_flota=0
        disparos_repetidos=0
        disparos_realizados=0
        puntaje=0
        '''Funcion para generar los disparos y validarlos'''
        while True:
            while True:
                try:
                    ingresar_fila= int(input('Fila: '))
                    ingresar_columna= int(input('Columna: '))
                    disparos_realizados+=1
                    if disparos_realizados==70:
                        print('Son muchos disparos. Perdiste')
                        break
                    
                    if ingresar_fila<0 or ingresar_columna<0 or ingresar_fila>10 or     ingresar_columna>10:
                        print('Esto no existe')

                    elif tablero[(ingresar_fila)][(ingresar_columna)]=='P':
                        oceano[(ingresar_fila)][(ingresar_columna)]='F'
                        print_tablero(oceano)
                        puntaje+=10
                        hundir_flota+=1
                        print('Hundiste un barco')
                    


                    else:
                        if oceano[(ingresar_fila)][(ingresar_columna)] == "X":
                            print('Ya la seleccionaste')
                            disparos_repetidos+=1
                        
                        else:
                            oceano[(ingresar_fila)][(ingresar_columna)] = "X"
                            print_tablero(oceano)
                            puntaje-=2
                            print('incorrecto')
                        
                    if hundir_flota==9:
                        break
                    
                except ValueError:
                    print('Ingresa un caracter valido')
            print(puntaje)
            break

   
    

    juego(oceano,tablero)



                

            

     
            
main()