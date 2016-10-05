from setuptools import setup
from setuptools import find_packages
from xsms import __author__, __email__, __url__, __version__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xsms',
    version=__version__,
    description='Xonotic Server Management Suite',
    long_description=readme,
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'': ['LICENSE', 'README.md', 'docs/*', 'config/*', 'bin/*']},
    include_package_data=True,
    install_requires=['pyyaml', 'screenutils'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
       'console_scripts': [
          'xsms = xsms.cli:main'
       ]
    },
)