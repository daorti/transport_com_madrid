from setuptools import setup, find_packages

with open('requirements.txt') as file:
    required = file.read().splitlines()

setup(name='BICIMAD_project',
      version='0.1.0',
      description='Proyecto encargado por la Com. Madrid para lanzar una app de Transporte',
      url='',
      author='rubenfernandezisla@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_dependencies=required)