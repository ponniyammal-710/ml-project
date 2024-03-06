from setuptools import find_packages ,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this funcion will return the list of the requirments
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

            return requirement 



setup(
    name='ml project',
    version='0.0.1',
    author='ponni',
    author_email='ponniyammalr30@gmail.com',
    packages_=find_packages(),
    install_requires=get_requirement('requirement.txt')


)