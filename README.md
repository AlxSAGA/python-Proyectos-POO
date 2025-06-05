# 🐍 Repositorio de Proyectos POO en Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![POO](https://img.shields.io/badge/Paradigma-POO-green)
![Proyectos](https://img.shields.io/badge/Proyectos-4-orange)

Este repositorio contiene una colección de proyectos prácticos que implementan los principios fundamentales de Programación Orientada a Objetos (POO) en Python. Cada proyecto representa un sistema completo que demuestra cómo aplicar conceptos avanzados de POO en escenarios del mundo real.

## 🧩 Proyectos Incluidos

### 📚 [1. Sistema de Biblioteca](biblioteca/)
Implementación de un sistema de gestión de biblioteca con enfoque en herencia y encapsulación.

```python
# Ejemplo de clase base
class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo  # Atributo protegido
        self.autor = autor
        self.isbn = isbn
    
    @property
    def titulo(self):
        return self._titulo
    
    def mostrar_info(self):
        return f"{self.titulo} por {self.autor}"
```

**Conceptos POO aplicados:**
- Encapsulación con atributos protegidos
- Uso de propiedades (`@property`)
- Herencia para diferentes tipos de libros
- Composición con relación Biblioteca-Libros

---

### 📝 [2. Gestión de Notas](GestionNotas/)
Sistema completo para administrar notas con persistencia de datos y métodos especiales.

```python
class Nota:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_creacion = datetime.now()
    
    def __str__(self):
        return f"[{self.fecha_creacion}] {self.titulo}"
    
    def editar(self, nuevo_contenido):
        self.contenido = nuevo_contenido
        self.fecha_modificacion = datetime.now()
```

**Conceptos POO aplicados:**
- Métodos especiales (`__str__`, `__repr__`)
- Persistencia de objetos con serialización
- Gestión de colecciones de objetos
- Validación de datos en setters

---

### 🚗 [3. Administración de Vehículos](vehicleAdministration/)
Sistema modular para gestión de flota vehicular con polimorfismo.

```python
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    @abstractmethod
    def obtener_tipo(self):
        pass

class Automovil(Vehiculo):
    def obtener_tipo(self):
        return "Automóvil"
```

**Conceptos POO aplicados:**
- Clases abstractas (`ABC`)
- Polimorfismo en métodos
- Herencia múltiple para vehículos especializados
- Métodos estáticos para validaciones

---

### 🐾 [4. Sistema Veterinario](veterinaria/)
Gestión de animales en una clínica veterinaria con enfoque en herencia.

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        raise NotImplementedError("Método abstracto")

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
```

**Conceptos POO aplicados:**
- Sobrescritura de métodos
- Jerarquías de herencia complejas
- Métodos de clase para estadísticas
- Decoradores para manejo de excepciones

## 🚀 Cómo Ejecutar los Proyectos

### Requisitos Previos
- Python 3.8+
- pip (Gestor de paquetes de Python)

### Instalación y Ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/AlxSAGA/pythonProyectosPOO.git
   cd pythonProyectosPOO
   ```

2. Configurar entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac)
   venv\Scripts\activate     # Windows
   ```

3. Instalar dependencias para un proyecto específico:
   ```bash
   cd biblioteca
   pip install -e .
   ```

4. Ejecutar el proyecto:
   ```bash
   python -m libros.main
   ```

## 🧪 Estructura de Proyecto Típica

Cada proyecto sigue una estructura modular consistente:

```
nombreProyecto/
├── README.md             # Documentación específica del proyecto
├── setup.py              # Configuración de paquete instalable
└── moduloPrincipal/      # Paquete Python
    ├── __init__.py       # Inicialización del paquete
    ├── classes.py        # Definición de clases principales
    ├── functions.py      # Funciones utilitarias
    ├── main.py           # Punto de entrada del programa
    └── utils.py          # Utilidades adicionales (si aplica)
```

## 💡 Mejores Prácticas Implementadas

1. **Encapsulación rigurosa**
   - Uso de atributos protegidos (`_variable`)
   - Implementación de propiedades con `@property`
   - Validación de datos en setters

2. **Diseño modular**
   - Separación clara de responsabilidades
   - Paquetes autocontenidos
   - Código fácilmente extensible

3. **Documentación integrada**
   - Docstrings en todas las clases y métodos
   - READMEs específicos por proyecto
   - Ejemplos de uso en documentación

4. **Manejo profesional de excepciones**
   - Excepciones personalizadas por dominio
   - Manejo adecuado de errores
   - Mensajes de error informativos

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b nueva-feature`)
3. Realiza tus cambios y haz commit (`git commit -am 'Agrego nueva funcionalidad'`)
4. Push a la rama (`git push origin nueva-feature`)
5. Abre un Pull Request

**Por favor asegúrate de:**
- Mantener la estructura de proyecto existente
- Documentar cualquier nueva característica
- Mantener coherencia en el estilo de código (PEP 8)
- Incluir pruebas para nuevas funcionalidades

