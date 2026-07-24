from setuptools import setup,find_packages
from typing import List


requirements="requirements.txt"
hypen_e_dot="-e ."

def get_requirements()->List[str]:

    with open(requirements) as requirements_file:

        requirements_list=requirements_file.readlines()
        requirements_list=[requirements_read.replace("\n","") for requirements_read in requirements_list]

        if hypen_e_dot in requirements_list:
            requirements_list.remove(hypen_e_dot)


        return requirements_list


setup(
    name='ML_PROJECT_MODULAR_CODING',
    version='0.0.1',
    description='I create a ML project using modular coding',
    author='Burhan Jalal',
    author_email='jalalburhan615@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)