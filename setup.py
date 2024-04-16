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
   install_requires=['SQLAlchemy~=2.0.29', 'fastapi~=0.110.1', 'pydantic~=2.6.4', 'pip~=24.0',
    'cryptography~=42.0.5'],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
<<<<<<< HEAD
)
=======
)
>>>>>>> origin/master
