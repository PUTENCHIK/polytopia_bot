from setuptools import setup

setup(
   name='polytopia_bot',
   version='0.5',
   description='Legendary the hardest bot for game The Battle of Polytopia',
   license='MIT',
   author='Maxim Olifirenko',
   author_email='opaolifirenkomaxim@gmail.com',
   url='https://github.com/PUTENCHIK/polytopia_bot',
   packages=['polytopia_bot', 'polytopia_bot/models'],
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
