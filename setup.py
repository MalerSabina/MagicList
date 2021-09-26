from setuptools import setup
from setuptools import find_packages

setup(
    name='pytest',
    version='0.1.0',
    packages=find_packages(include=['MagicList', 'requirements.txt']),
    install_requires=[
        'pytest'
    ]
)
