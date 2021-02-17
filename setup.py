from setuptools import setup, find_packages

setup(
    name='pbi-tools',
    version='0.1.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Power BI REST API wrapper and other tools',
    long_description=open('README.md').read(),
    install_requires=['requests','gitpython'],
    url='https://github.com/thomas-daughters/pbi-tools',
    author='Sam Thomas',
    author_email='sam.thomas@redkite.com'
)