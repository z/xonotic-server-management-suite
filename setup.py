from setuptools import setup
from setuptools import find_packages
from xsms import __author__, __email__, __url__, __license__, __version__, __summary__, __keywords__

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xsms',
    version=__version__,
    description=__summary__,
    long_description=readme,
    author=__author__,
    author_email=__email__,
    url=__url__,
    license=__license__,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'': ['LICENSE', 'README.md', 'docs/*', 'config/*', 'bin/*']},
    include_package_data=True,
    install_requires=['pyyaml', 'screenutils', 'libtmux', 'ptpython'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
       'console_scripts': [
          'xsms = xsms.cli:main'
       ]
    },
    keywords=__keywords__,
    classifiers=[
        'Intended Audience :: System Administrators',

        'License :: OSI Approved :: MIT License',

        'Development Status :: 4 - Beta',

        'Environment :: Console',

        'Topic :: Games/Entertainment',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)