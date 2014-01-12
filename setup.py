import os
import sys
from setuptools import setup, find_packages

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname)).read()

def desc():
    return read('README.rst')

setup(
    name='Flask-BabelPkg',
    version='0.9.2',
    url='http://github.com/dpgaspar/flask-babelPkg',
    license='BSD',
    author='Daniel Gaspar',
    author_email='danielvazgaspar@gmail.com',
    description='Adds i18n/l10n support to Flask applications and extensions',
    long_description=desc(),
    packages=['flask_babelpkg'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Babel>=1.0',
        'speaklater>=1.2',
        'Jinja2>=2.5'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
