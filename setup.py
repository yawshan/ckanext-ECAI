from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-ECAI',
    version=version,
    description="",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ECAI'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        ckanext_ECAI=ckanext.ECAI.plugin:ECAIPlugin
        timesearch=ckanext.ECAI.plugin:TimeSearchPlugin
        # Add plugins here, e.g.
        # myplugin=ckanext.ECAI.plugin:PluginClass
    ''',
)
