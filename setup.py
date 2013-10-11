from setuptools import setup, find_packages

setup(
    name='django-geo',
    version='0.0.1',
    description='Zip codes and basic geographic support library',
    author='Philip Kimmey',
    author_email='philip@rover.com',
    url='https://github.com/philipkimmey/django-geo',
    packages=find_packages(exclude=('tests', 'docs'))
)
