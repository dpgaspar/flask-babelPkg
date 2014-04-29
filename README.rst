Flask Babel Pkg
===============

.. image:: https://travis-ci.org/dpgaspar/flask-babelPkg.png?branch=master
	:target: https://travis-ci.org/dpgaspar/flask-babelPkg

Implements i18n and l10n support for Flask.  This is based on the Python
babel module as well as pytz both of which are installed automatically
for you if you install this library.

This is a fork from flask-babel, with a small change to support flask extensions translations.

With this you will have two diferent translations on the application, the extension translations and the application translations.

You can use it just like flask-babel orginal::

	app = Flask(__name__)
	babel = Babel(app)

Or you can use it in the package extension form::

	from flask.ext.yourpackage import translations

	babel = Babel(app, translations)


