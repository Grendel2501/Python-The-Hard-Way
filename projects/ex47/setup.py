try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Example 47 Project',
    'author': 'Richard Bakare',
    'url': 'http://www.richardbakare.com/...',
    'download_url': 'http://wwww.richardbakare.com/Downloads/',
    'author_email': 'info@richardbakare.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
