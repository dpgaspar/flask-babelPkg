"""
Flask-BabelPkg
-----------

Adds i18n/l10n support to Flask applications and extensions with the help of the
`Babel`_ library. Based on flask-babel, added support for flask extensions

Links
`````

* `documentation <http://packages.python.org/Flask-Babel>`_
* `development version
  <http://github.com/mitsuhiko/flask-babel/zipball/master#egg=Flask-Babel-dev>`_

.. _Babel: http://babel.edgewall.org/

"""
from setuptools import setup


setup(
    name='Flask-BabelPkg',
    version='0.9',
    url='http://github.com/dpgaspar/flask-babelPkg',
    license='BSD',
    author='Daniel Gaspar',
    author_email='danielvazgaspar@gmail.com',
    description='Adds i18n/l10n support to Flask applications and extensions',
    long_description=__doc__,
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
