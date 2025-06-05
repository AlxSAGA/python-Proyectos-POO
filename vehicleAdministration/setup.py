from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vehicle-manager",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu.email@ejemplo.com",
    description="Sistema de gestión de vehículos para terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/gestion-vehiculos",
    packages=find_packages(),
    install_requires=[
        'termcolor>=1.1.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Office/Business",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'vehicle-manager=main:main',
        ],
    },
    keywords='vehículos gestión alquiler inventario',
    project_urls={
        "Bug Tracker": "https://github.com/tu-usuario/gestion-vehiculos/issues",
    },
)
