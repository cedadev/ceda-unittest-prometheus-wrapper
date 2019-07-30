#!/usr/bin/env python
"""Distribution Utilities setup program for Prometheus target unit test case
wrapper
"""
__author__ = "P J Kershaw"
__date__ = "13/07/19"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"

# Bootstrap setuptools if necessary.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name =              'ceda-unittest-prometheus-wrapper',
    version =           '0.1.1',
    description =       'Prometheus wrapper for unittest test case',
    long_description =  '''Allows easy creation of a wrapper script to a unit
test case so that it can act as a Prometheus target
''',
    author =            'Philip Kershaw',
    author_email =      'Philip.Kershaw@stfc.ac.uk',
    maintainer =        'Philip Kershaw',
    maintainer_email =  'Philip.Kershaw@stfc.ac.uk',
    platforms =         ['POSIX', 'Linux', 'Windows'],
    install_requires =  ['prometheus_client'],
    license =           __license__,
    test_suite =        '',
    packages =          find_packages(),
    package_data={
        'ceda/cci_odp_ops_tests': [
            'LICENSE',
        ],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'prometheus_unittest_wrapper = '
            'ceda.unittest_prometheus_wrapper.script:main',
        ],
    },
    zip_safe = False
)
