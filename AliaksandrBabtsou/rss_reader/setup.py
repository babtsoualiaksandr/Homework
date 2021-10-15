from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = 'Feed Parser'
LONG_DESCRIPTION = 'Python RSS-reader using python 3.9.'

setup(
    name="rss-reader",
    version=VERSION,
    author="Aliaksandr Babtsou",
    author_email="babtsoualiaksandr@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages('src'),
    include_package_data=True,
    package_data={
        'src': ['static/*.*'],
    },
    install_requires=['requests', 'python-dateutil', 'fpdf2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    keywords=['python', 'feed parser'],
    entry_points={
        'console_scripts':  ['rss_reader = src.rss_reader: main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ]

)
