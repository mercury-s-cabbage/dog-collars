from setuptools import setup

setup(
   name='first_setup',
   version='1.0',
   description='Trying to make setup for good marks)',
   license='MIT',
   author='Lena Filipenko',
   author_email='lenaphilip@mail.ru',
   url='https://github.com/mercury-s-cabbage/dog-collars',
   packages=['src'],
   install_requires=[],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
