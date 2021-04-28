from setuptools import setup

setup(
    name = 'imvickykumar999', # while installing pacakge, change name to something unique on pypi.org
    version = '0.0.4', # use different version if updated, like '0.0.8'

    description = 'Website : https://github.com/imvickykumar999/Firebase-CRUD',
    long_description = open('README.md').read(),

    url = 'https://imvickykumar999.herokuapp.com/news',
    author = 'Vicky Kumar',

    keywords = ['Firebase', 'Playfair Cipher', 'GitHub Uploader', 'Morse',
    'Vector', 'python package', 'function and class', '3D line',
    '3D plane', 'angle b/w planes or line', 'distance bw point and plane'],

    license = 'MIT',
    packages = ['multivicks', 'vicksbase'], # while importing package
    install_requires = ['']
)
