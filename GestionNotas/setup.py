from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='alx-notes',
    version='1.0.0',
    author='Tu Nombre',
    author_email='tu@email.com',
    description='Gestor de notas para estudiantes ALX - Command Line Interface',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tuusuario/alx-gestor-notas',
    packages=find_packages(),
    install_requires=[
        'termcolor>=1.1.0',
    ],
    entry_points={
        'console_scripts': [
            'alx-notes=appNotas.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Education',
        'Topic :: Utilities'
    ],
    python_requires='>=3.6',
    keywords='alx notes organizer cli',
)
