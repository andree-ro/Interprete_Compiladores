import os # proporciona funcionalidad para interactur con el sistema operativo
import datetime # para hora y fecha
#cimport shutil
import platform # que proporciona información sobre la plataforma y el sistema operativo en el que se ejecuta el programa


def main():
    # el metodo .startswitch() se utilizar para verificar si el comando comienza con ciertos caracteres.
    while True:
        comando = input("> ")
        if comando == "pwd":
            print(os.getcwd())
        elif comando == "date":
            print(datetime.date.today())
        elif comando == "time":
            print(datetime.datetime.now().time())
        elif comando == "exit":
            break
        elif comando == "clear":
            clear_screen()
        elif comando == "man":
            mostrar_ayuda()
        elif comando == "uname -a":
            mostrar_version_os()
        elif comando.startswith("cd"):
            cambiar_directorio(comando)
        elif comando.startswith("ls"):
            listar_directorio(comando)
        elif comando.startswith("rm "):
            borrar_archivo(comando)
        elif comando.startswith("mkdir "):
            crear_directorio(comando)
        elif comando.startswith("rmdir "):
            borrar_directorio(comando)
        else:
            print("Comando no reconocido")


def clear_screen():
    os.system("cls") # Borramos lo que esta en consola.


def mostrar_ayuda():
    print("Comandos permitidos:")
    print("1. pwd - Muestra el directorio activo.")
    print("2. date - Muestra la fecha actual.")
    print("3. time - Muestra la hora actual.")
    print("4. exit - Sale del intérprete o programa.")
    print("5. clear - Borra la pantalla.")
    print("6. man - Proporciona ayuda de los comandos.")
    print("7. uname -a - Muestra la versión del OS.")
    print("8. cd [directorio] - Cambia el directorio activo.")
    print("9. ls [opciones][dir] - Muestra el contenido del directorio especificado.")
    print("10. rm [archivos] - Borra archivos.")
    print("11. mkdir [directorio] - Crea un directorio.")
    print("12. rmdir [directorio] - Borra un directorio.")


def mostrar_version_os():
    system_info = platform.uname() # inicializamos el objeto
    print("Sistema operativo:", system_info.system)
    print("Nombre del nodo:", system_info.node)
    print("Versión del sistema:", system_info.release)
    print("Versión del sistema detallada:", system_info.version)
    print("Arquitectura del hardware:", system_info.machine)
    print("Procesador:", system_info.processor)


def cambiar_directorio(comando):
    partes = comando.split(" ")
    if len(partes) == 1: # Verifica si el comando se ingresó sin argumentos adicionales
        os.chdir(os.path.expanduser("~")) # obtenemos la ruta completa del directorio personal y lo establecemos como directorio activo
    elif len(partes) == 2: # Verifica si el comando tiene dos partes
        try:
            os.chdir(partes[1]) # cambiamos el directorio actual al directorio puesto en partes[1]
        except FileNotFoundError:
            print(f"Directorio no encontrado: {partes[1]}")
    else:
        print("Uso incorrecto de cd. Uso: cd [directorio]")


def listar_directorio(comando):
    partes = comando.split(" ")
    opciones = "" # inicializamos una cadena vacia, nos servira para almacenar -a o -l
    directorio = os.getcwd() # obtenemos el directorio

    if len(partes) > 1: # Verifica si el usuario agrego opciones adicionales
        opciones = partes[1]
        # Si el usuario proporcionó solo el comando "ls" o "ls -a", el directorio activo se establece en el directorio
        # de trabajo actual (os.getcwd()). Si el usuario proporcionó un tercer argumento (como "ls -l directorio"), se
        # establece directorio en ese tercer argumento (el nombre del directorio proporcionado por el usuario).
        directorio = os.getcwd() if len(partes) == 2 else partes[2]
    try:
        with os.scandir(directorio) as archivos: # escaneamos el contenido del directorio especificado y devuelve un contenido iterable
            for archivo in archivos:
                # Verifica si esta -a o si el nombre del archivo no comienza con punto  (lo que significa que no es un archivo oculto).
                if opciones == "-a" or not archivo.name.startswith("."):
                    if opciones == "-l": # si tiene -l muestra caracteristicas del archivo
                        print(archivo.name, archivo.stat())
                    else:
                        print(archivo.name)
    except FileNotFoundError:
        print(f"Directorio no encontrado: {directorio}")


def borrar_archivo(comando):
    partes = comando.split(" ") # cada linea la metemos a una lista
    if len(partes) > 1: # si los elementos de la lista es mayor a 1
        archivos = partes[1:] # nueva lista con los elementos de la posicion 1 a la posicion n
        for archivo in archivos: # recorremos lista
            try:
                os.remove(archivo) # encontramos el archivo que queremos borrar y lo borramos
                print(f"Archivo borrado: {archivo}")
            except FileNotFoundError:
                print(f"Archivo no encontrado: {archivo}")
            except PermissionError:
                print(f"No tienes permisos para borrar: {archivo}")
    else:
        print("Uso incorrecto de rm. Uso: rm [archivo]")


def crear_directorio(comando):
    partes = comando.split(" ")
    if len(partes) == 2: # si la lista tiene tamanio 2
        try:
            os.mkdir(partes[1]) # creamos el directorio con el nombre especifico
            print(f"Directorio creado: {partes[1]}")
        except FileExistsError:
            print(f"El directorio ya existe: {partes[1]}")
    else:
        print("Uso incorrecto de mkdir. Uso: mkdir [directorio]")


def borrar_directorio(comando):
    partes = comando.split(" ")
    if len(partes) == 2: # si la lista tiene tamanio 2
        try:
            os.rmdir(partes[1]) # borramos el directorio requerido
            print(f"Directorio borrado: {partes[1]}")
        except FileNotFoundError:
            print(f"Directorio no encontrado: {partes[1]}")
        except OSError:
            print(f"No se puede borrar el directorio: {partes[1]}")
    else:
        print("Uso incorrecto de rmdir. Uso: rmdir [directorio]")


if __name__ == "__main__":
    main()
