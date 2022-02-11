

from setuptools import setup, find_packages

with open('requirements.txt') as file:
    required = file.read().splitlines()

setup(name='transporte_ayto_madrid',
      version='0.1.0',
      description='Información de estaciones de Tte. Público',
      url='',
      author='Antonio Jiménez',
      author_email='antonio.jimenez@the-cocktail.com',
      license='MIT',
      packages=find_packages(),
      install_requirements=required)