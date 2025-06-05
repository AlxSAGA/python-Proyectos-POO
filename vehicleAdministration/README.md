```markdown
# 🚗 Sistema de Gestión de Vehículos

¡Bienvenido al **Sistema de Gestión de Vehículos**! Este programa te permite administrar un inventario de vehículos, incluyendo opciones para rentar, devolver y visualizar su disponibilidad. Desarrollado en Python para terminal, con una interfaz colorida y amigable.

---

## 📋 Descripción

Este proyecto es un sistema de gestión para vehículos que permite:
- Agregar nuevos vehículos al inventario.
- Mostrar todos los vehículos registrados.
- Rentar y devolver vehículos.
- Limpiar la pantalla y salir del programa.

Ideal para talleres, concesionarios o cualquier negocio que necesite gestionar flotas de vehículos de forma sencilla.

---

## 🛠️ Características Principales

- **Menú interactivo** con opciones numeradas.
- **Colores en terminal** para mejor legibilidad (`termcolor`).
- **Validación de disponibilidad** al rentar/devolver vehículos.
- **Persistencia de datos** mientras el programa esté en ejecución.

---

## 📦 Requisitos Previos

- Python 3 instalado.
- Librería `termcolor` para colores en terminal.

```bash
pip install termcolor
```

---

## 🚀 Instalación

1. Clona el repositorio o descarga los archivos.
2. Ejecuta el programa desde tu terminal:

```bash
git clone https://github.com/AlxSAGA/gestion-vehiculos.git
cd gestion-vehiculos
python3 main.py
```

---

## 🖥️ Uso

### Menú Principal
```
[+] Select an option: 
(1)Add Vehicle - (2)Show Vehicles - (3)Rent a Vehicle - (4)Return the Vehicle - (5)Clean Screen - (0)Finish Program
```

### Opciones Detalladas
1. **Agregar Vehículo**:  
   Ingresa matrícula, marca y modelo.
2. **Mostrar Vehículos**:  
   Lista todos los vehículos con su estado (disponible/no disponible).
3. **Rentar Vehículo**:  
   Introduce la matrícula para marcar como "no disponible".
4. **Devolver Vehículo**:  
   Usa la matrícula para marcar como "disponible".
5. **Limpiar Pantalla**:  
   Borra el contenido de la terminal.
0. **Salir**:  
   Finaliza el programa.

---

## 📂 Estructura del Proyecto

- `main.py`: Contiene el flujo principal del programa y el menú.
- `classes.py`: Define las clases `Vehicle` (vehículo individual) y `VehicleStorage` (gestión de la lista).
- `functions.py`: Funciones auxiliares (limpiar pantalla, controlar salida, etc.).

---

## 👥 Contribuciones

¡Contribuciones son bienvenidas! Sigue estos pasos:
1. Haz un fork del proyecto.
2. Crea una rama con tu feature (`git checkout -b feature/nueva-funcion`).
3. Haz commit de tus cambios (`git commit -m 'Añade nueva función'`).
4. Haz push a la rama (`git push origin feature/nueva-funcion`).
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar el **Sistema de Gestión de Vehículos**! 🚀  
Desarrollado con ❤️ por [Alex Salazar].
```
