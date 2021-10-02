from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Feed Parser'
LONG_DESCRIPTION = ''

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="rss-reader",
    version=VERSION,
    author="Aliaksandr Babtsou",
    author_email="babtsoualiaksandr@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords=['python', 'feed parser'],
    entry_points={
        'console_scripts':  ['rss_reader = rss_reader.rss_reader: main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",

    ]

)
