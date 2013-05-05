from setuptools import setup

setup(
    name='war',
    version='1.0',
    entry_points={
        'console_scripts': [
            'war = war:main'
        ]
    },
    test_suite='war.test',
    packages=['war'],
    license=open('LICENSE').readline(),
    long_description=open('README.mdown').read(),
)
