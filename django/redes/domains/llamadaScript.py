import os
from os import remove

#CREACION DE NUEVOS DOMINIOS
def NuevoDomino(nombreUsuario, contraseña, nombreDominio):
    #directorio = nombreUsuario
    #directorio = "../../../"+ nombreUsuario
    directorio = "../../../DominiosC/"+ nombreUsuario
    if os.path.isdir(nombreUsuario):
        return 1
    else:
        try:
            os.mkdir(directorio)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            return 0


#CREACION DE ARCHIVOS DEL CLIENTE
def creacionArchivos(nombre, contraseña, Dominio,user):
    #directorio = "../../../"
    directorio = "../../../DominiosC/"
    #if os.path.isfile(nombre + "/" + Dominio + ".txt"):
    if os.path.isfile( directorio + nombre + "/" + Dominio + ".txt"):
        print('El archivo existe.')
    else:
        f = open(directorio + nombre + "/" + Dominio + ".txt", "w")
        insertar(user, contraseña, Dominio, f)
        f.close

def insertar(user, contraseña, dominio, file):
    file.write("Usuario:  ")
    file.write(user)
    file.write("\n")
    file.write("Contraseña:  ")
    file.write(contraseña)
    file.write("\n")
    file.write("Dominio:  ")
    file.write(dominio)
    file.close()


#EDICION DE ARCHIVOS DE DOMINIO

    #EDICION DE NOMBRE DE NOMBRE DE DOMINIO
def EditarNombreDominio(nombre, contraseña, dominio,user,nombrenuevo):
    archivo = nombre + "/" + dominio + ".txt"
    nombre_nuevo = nombre + "/" + nombrenuevo + ".txt"
    try:
        os.rename(archivo, nombre_nuevo)
        f = open(nombre + "/" + nombrenuevo + ".txt", "w")
        insertar(user,contraseña,nombrenuevo,f)
        print("Se ha cambiado el nombre del dominio")
    except OSError:
        print("Ya existe este dominio")

#EDICION DE CONTRASEÑA DE DOMINIO
def editarContraseñaDominio(nombre, contraseña, dominio,user,contraseñanueva):
    archivo = nombre + "/" + dominio + ".txt"
    try:
        f = open(nombre + "/" + dominio + ".txt", "w")
        insertar(user,contraseñanueva,contraseñanueva,f)
        print("Se ha cambiado la contraseña")
    except OSError:
        print("No se pudo cambiar la contraseña")

#EDICION DE NOMBRE DE USUARIO
def editarNombreUsuario(nombre, contraseña, dominio,user,usernuevo):
    archivo = nombre + "/" + dominio + ".txt"
    try:
        f = open(nombre + "/" + dominio + ".txt", "w")
        insertar(usernuevo,contraseña,dominio,f)
        print("Se ha cambiado el usuario")
    except OSError:
        print("No se pudo cambiar el usuario")


#ELIMINAR DOMINIO
def EliminarDominio(nombre,dominio):
    remove(nombre + "/" + dominio  + ".txt")






def main(nombre,contraseña,dominio,usuario):
    dir1 = "../../../DominiosC"
    if os.path.isdir(dir1):
        print("")
    else:
        try:
            os.mkdir(dir1)
        except OSError:
            print("La creación del directorio %s falló" % dir1)
    
    path = os.getcwd()
# # Se define el nombre de la carpeta o directorio a crear
    bool = NuevoDomino(nombre,contraseña,dominio)
    print(path)
# #SI RETORNA 1 EL DIRECTORIO EXISTE SINO SE CREA
    if (bool == 1):
        print("La creación del directorio falló" + " Este ya existe")
    else:
        print("Se ha creado el directorio ")

    #CREA ARCHIVOS PARA EL DOMINIO QUE SE INDIQUE
    creacionArchivos(nombre, contraseña, dominio, usuario)
    # creacionArchivos("Gilda", "contraseña", "Clinica","Usuario2")
    # creacionArchivos("Gilda", "contraseña", "Cafe2","Usuario3")

    # EditarNombreDominio("Gilda", "contraseña", "Cafe2","Usuario", "Bar")
    # #editarContraseñaDominio("Gilda", "contraseña", "Bar", "Usuario","nuevacontra")
    # #editarNombreUsuario("Gilda", "contraseña", "Bar", "Usuario","CAJA")
    # EliminarDominio("Gilda", "Cafe2")