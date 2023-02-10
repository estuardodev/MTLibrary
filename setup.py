from setuptools import find_packages, setup
# read the contents of your README file
from pathlib import Path
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



setup(
    name='mtlibrary',
    version='2.0.5',
    description='MTLibrary es una libreria en español desarrollada para resolver problemas matemáticos y así ayudar a esos programadores con bajos conocimientos con librerias en inglés.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author='Estuardo Ramírez',
    author_email='estuardo@estuardodev.com',
    url='https://github.com/estuardodev/MTLibrary',
    download_url='https://github.com/estuardodev/MTLibrary.git',
    keywords=['estuardodev', 'mtlibrary', 'matematicas', 'math'],
    packages=find_packages(),
    classifiers = [
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    py_modules=['mtlibrary'],
    requires_python = ">=3.9"
)