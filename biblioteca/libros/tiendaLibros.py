#!/usr/bin/env python3

# Librerias
from termcolor import colored as color

# Clase principal
class Libro:

    def __init__(self, id_libro: int, autor: str, titulo: str):
        
        self.id_libro = id_libro
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):

        return color(f"Libro: ( {self.id_libro} ), ( {self.autor} ), ( {self.titulo} )", "green")

    def __repr__(self):
        
        return self.__str__()

# Clase que representa la Biblioteca DE LIBROS (Contiene la coleccion)
class Biblioteca:
    
    def __init__(self):

        # Aqui se agregaran los nuevos libros.
        self.libros_programacion = {
            1: Libro(1, "Clean Code", "Robert C. Martin"),
            2: Libro(2, "The Pragmatic Programmer", "Andrew Hunt, David Thomas"),
            3: Libro(3, "Design Patterns", "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides"),
            4: Libro(4, "Code Complete", "Steve McConnell"),
            5: Libro(5, "Refactoring", "Martin Fowler"),
            6: Libro(6, "Head First Design Patterns", "Eric Freeman, Elisabeth Robson"),
            7: Libro(7, "Introduction to Algorithms", "Thomas H. Cormen"),
            8: Libro(8, "Structure and Interpretation of Computer Programs", "Harold Abelson, Gerald Jay Sussman"),
            9: Libro(9, "You Don't Know JS", "Kyle Simpson"),
            10: Libro(10, "The Art of Computer Programming", "Donald Knuth")
        }


    # Metodo para agregar libros
    def agregar_libro(self, libro: Libro):

        if libro.id_libro not in self.libros_programacion:
            
            self.libros_programacion[libro.id_libro] = libro

            print(color(f"[+] Nuevo libro agregador correctamente...", "blue"))

        else:
            
            print(color(f"\n[-] No es posible agregar el libro con ID: ( {libro.id_libro} )", "red"))

    # Metodo para prestar libros
    def prestar_libro(self, id_libro):

        if id_libro in self.libros_programacion and not self.libros_programacion[id_libro].esta_prestado:
        
            self.libros_programacion[id_libro].esta_prestado = True

            print(color("\n[+] Prestamo autorizado correctamente...", "blue"))
        
        else:

            print(color(f"[-] Actualmente el libro con identificador: ( {id_libro} ) no esta disponible...", "red"))

    # Metod para mostrar libros 
    @property
    def mostrar_libros_disponibles(self):
        """The mostar_libros_disponibles property."""
        return [libro for libro in self.libros_programacion.values() if not libro.esta_prestado]

    # Metod para mostrar libros prestados 
    @property
    def mostrar_libros_prestados(self):
        """The mostar_libros_prestado property."""
        return [libro for libro in self.libros_programacion.values() if libro.esta_prestado]

