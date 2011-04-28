from setuptools import setup, find_packages

version = 'Unknown'

setup(
    name = 'cmsplugin-flickr',
    version = version,
    description = 'flickr plugin for django-cms',
    author = 'Unknown',
    author_email = '',
    packages = find_packages(),
    zip_safe=False,
    install_requires=[
        'Django>=1.2',
        'django-cms',
    ],
)
