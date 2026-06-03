from setuptools import setup,find_packages
from typing import List

requirements_1st:List[str]=[]
def get_requirements()->List[str]:
    try:
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != '-e .':
                    requirements_1st.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements_1st

print(get_requirements())

setup(
    name='Network Security',
    version='0.0.1',
    Author='Shubham Upadhyay',
    author_mail='shubham101upadhyay@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)