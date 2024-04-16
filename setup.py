from setuptools import setup, find_packages

setup(
   name='polytopia_bot',
   version='0.5',
   description='Legendary the hardest bot for game The Battle of Polytopia',
   license='MIT',
   author='Maxim Olifirenko',
   author_email='opaolifirenkomaxim@gmail.com',
   url='https://github.com/PUTENCHIK/polytopia_bot',
   packages=find_packages(exclude=['tests']),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
