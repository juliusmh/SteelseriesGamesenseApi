#from distutils.core import setup
from setuptools import setup

setup(
    name='Python-Gamesense-API',
    version='0.1.0',
    author='juliusmh',
    packages=["pygamesense"],
    url='http://github.com/juliusmh/Python-Gamesense-API',
    description='A simple wrapper for SteelSeries\'s GameSense API',
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ]
)
