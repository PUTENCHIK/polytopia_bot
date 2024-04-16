from setuptools import setup

setup(
   name='polytopia-bot',
   version='0.5',
   description='Legendary the hardest bot for game The Battle of Polytopia',
   license='MIT',
   author='Maxim Olifirenko',
   author_email='opaolifirenkomaxim@gmail.com',
   url='https://github.com/PUTENCHIK/polytopia-bot',
   packages=['mtracker'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
