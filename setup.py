from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:  # Correctly use List from typing
    requirements_list: List[str] = []  # Proper type hinting for a variable
    return requirements_list

setup (
    name= 'sensor',
    version='0.0.1',
    author='Muneeb',
    author_email='muneebshahzad9693@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements()#['pymongo']
)