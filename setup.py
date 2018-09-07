from setuptools import find_packages, setup

__author__ = 'peter'

install_requires = open('requirements.txt').read().splitlines()

setup(
    # name of application
    name='assignment',
    # version number goes here
    version='0.0.1',
    # Authors name
    author='Edache Peter',
    # author email address
    author_email='peter.edac@gmail.com',

    packages=find_packages(exclude=['tests*']),

    # include additional files into the package
    include_package_data=True,

    url="http://finetune.ii",

    install_requires=install_requires,
    entry_points={
        'console_scripts': []
    },
    classifiers=[
        'Private :: Dont upload to any pypi registry'
    ]

)

