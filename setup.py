from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''Returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


    return requirements



setup(
name='End-to-end-ML-Project',
version='0.0.1',
author='Shashank',
author_email='shashankkumar2160@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)