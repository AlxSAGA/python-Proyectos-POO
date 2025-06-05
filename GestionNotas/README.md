```markdown
# Gestor de Notas ALX

Aplicación de línea de comandos para organización de apuntes estudiantiles. Desarrollado en Python con programación orientada a objetos.

## Características Principales

- **Agregar notas**: Crear nuevas notas con entrada simple de texto
- **Leer notas**: Visualizar todas las notas guardadas con sus índices
- **Buscar notas**: Encontrar notas que contengan palabras específicas
- **Eliminar notas**: Remover notas mediante su índice numérico
- **Almacenamiento persistente**: Guardado automático usando serialización con pickle
- **Interfaz intuitiva**: Menús colorizados y claros
- **Manejo de interrupciones**: Control adecuado de Ctrl+C

## Instalación

1. **Clonar repositorio**:
   ```bash
   git clone https://github.com/AlxSAGA/alx-gestor-notas.git
   cd alx-gestor-notas
   ```

2. **Instalar dependencias**:
   ```bash
   pip install termcolor
   ```

3. **Permisos de ejecución** (Opcional):
   ```bash
   chmod +x main.py
   ```

## Uso

```bash
./main.py
```

**Opciones del Menú Principal**:
```
(1) Agregar Nota - (2) Ver Notas - (3) Buscar Nota - (4) Eliminar Nota - (5) Limpiar Pantalla - (0) Salir
```

- **Agregar Nota**: Escribe texto para crear nueva nota
- **Ver Notas**: Muestra todas las notas con sus índices
- **Buscar Notas**: Filtra notas que contengan el término buscado
- **Eliminar Nota**: Borra nota por número de índice
- **Limpiar Pantalla**: Borra el contenido de la terminal
- **Salir**: Finaliza el programa correctamente

## Estructura del Proyecto

```
.
├── main.py            # Punto de entrada principal
├── classes.py         # Clase NotesManager
├── notes.py           # Clase Note
├── functions.py       # Funciones auxiliares y menús
└── notes.pkl          # Almacenamiento de datos (auto-generado)
```

## Dependencias

- Python 3.x
- [termcolor](https://pypi.org/project/termcolor/) - Para colores en consola
- pickle (Biblioteca estándar de Python)

## Cómo Contribuir

1. Haz un fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/NuevaFuncion`)
3. Realiza tus cambios (`git commit -m 'Agrega NuevaFuncion'`)
4. Publica la rama (`git push origin feature/NuevaFuncion`)
5. Abre un Pull Request

## Licencia

Distribuido bajo licencia MIT. Ver `LICENSE` para más detalles.

## Notas Importantes

- Los datos se guardan en `notes.pkl` usando serialización
- Manejo profesional de interrupciones de teclado
- Interfaz colorizada para mejor experiencia de usuario
- Validación de entradas para índices y selecciones de menú
- Sistema multiplataforma (Windows/Linux/macOS)
```
