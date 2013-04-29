from setuptools import setup

setup(
    name = 'war',
    version = '1.0',
    entry_points = {
        'console_scripts': [
            'war = war:main'
        ]
    },
    test_suite = 'war.tests',
    packages = ['war'],
    license = open('LICENSE').read(),
    long_description = open('README.mdown').read(),
)
