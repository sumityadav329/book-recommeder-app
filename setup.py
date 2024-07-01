from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return requirements

setup(
    name='books-recommender',
    version='0.0.1',
    author='Sumit',
    author_email='sumityadav329@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A WebApp for Recommending books',
    url='https://github.com/sumityadav329/book-recommender-app'
)
