
**setup.py**
```python
from setuptools import setup, find_packages

setup(
    name="biblioteca-mexicana",
    version="0.1.0",
    author="alex salazar",
    description="Sistema de gestión para bibliotecas",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/biblioteca-mexicana",
    packages=find_packages(),
    install_requires=[
        "termcolor>=1.1.0",
    ],
    entry_points={
        'console_scripts': [
            'biblioteca-mexicana = bibliotecamexicana.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
