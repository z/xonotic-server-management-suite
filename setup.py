from setuptools import setup
from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xsms',
    version='0.2.0',
    description='Xonotic Server Management Suite',
    long_description=readme,
    author='Tyler Mulligan',
    author_email='z@xnz.me',
    url='https://github.com/z/xonotic-server-management',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
       'console_scripts': [
          'xsms = xsms.bin:main'
       ]
    },
    install_requires=['pyyaml']
)