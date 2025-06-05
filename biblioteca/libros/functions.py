#!/usr/bin/env python3

# Librerias
import sys, signal, os
from termcolor import colored as color

# Funciones personalizadas
def ctrl_c(signal, frame):

    print(color(f"\n\n[-] Saliendo...", "red"))
    sys.exit(1)

# ctrl_c
signal.signal(signal.SIGINT, ctrl_c)

def terminar_programa():

    print(color(f"\n\n[+] Programa terminado correctamente...", "green"))
    sys.exit(0)

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")
