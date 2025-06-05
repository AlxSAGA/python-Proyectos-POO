#!/usr/bin/env python3

# Librerias
import time
from termcolor import colored as color

# Funciones Personales Importadas
from functions import ctrl_c, terminar_programa, limpiar_pantalla

# Importacion metodos de la clase Libro
from tiendaLibros import Libro, Biblioteca

# Funcion pricipal
def main():

    print(color(f"\n[+] Bienvenidos a bibliotecaMexicana", "cyan"))

    # Instancioa de la biblioteca
    biblioteca = BibliotecaJunior()
    
    while True:

        option = str(input("\n[*] Selecciona una opcion: (1)agregarLibro - (2)prestarLibro - (3)verLibros - (4)verLibrosPrestados - (5)limpiarPantalla - (0)terminarPrograma\n\n==>   "))

        if option == "1":
            
            id_libro = int(input("\n[+] Ingresa el ( ID ):  "))
            titulo_libro = str(input("\n[+] Ingresa el titulo del libro:  "))
            autor_libro = str(input("\n[+] Ingresa el nombre del autor:  "))

            libro = Libro(id_libro, titulo_libro, autor_libro)


            biblioteca.agregar_libro(libro)

        elif option == "2":

            for prestar_libro in biblioteca.mostrar_libros_disponibles:
                print(prestar_libro)

            option_id = int(input("\n\n[+] Ingresa el identificador del libro: "))

            biblioteca.prestar_libro(option_id)

        elif option == "3":

            for libro_disponible in biblioteca.mostrar_libros_disponibles:
                print(libro_disponible)

        elif option == "4":

            for libro_prestado in biblioteca.mostrar_libros_prestados:
                print(libro_prestado)

        elif option == "5":

            limpiar_pantalla()

        elif option == "0":

            terminar_programa()

        else:
            
            print(color(f"\n[-] Erro: Opcion invalida...", "red"))

# Flujo proncipal del programa
if __name__ == "__main__":
    main()
