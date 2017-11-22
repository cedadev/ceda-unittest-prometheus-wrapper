#!/usr/bin/env python
"""Distribution Utilities setup program for CCI OGC CSW ops test package

Contrail Project
"""
__author__ = "P J Kershaw"
__date__ = "21/11/17"
__copyright__ = "(C) 2017 Science and Technology Facilities Council"
__license__ = """BSD - See LICENSE file in top-level directory"""
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = '$Id$'

# Bootstrap setuptools if necessary.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name =              'ceda-unittest-nagios-wrapper',
    version =           '0.1.0',
    description =       'Nagios wrapper for unittest test case',
    long_description =  '''Allows easy creation of a wrapper script to a unit
test case so that it can be called from Nagios or Icinga
''',
    author =            'Philip Kershaw',
    author_email =      'Philip.Kershaw@stfc.ac.uk',
    maintainer =        'Philip Kershaw',
    maintainer_email =  'Philip.Kershaw@stfc.ac.uk',
    platforms =         ['POSIX', 'Linux', 'Windows'],
    install_requires =  ['nagiosplugin'],
    license =           __license__,
    test_suite =        '',
    packages =          find_packages(),
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
        'Programming Language :: Python :: 2',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'cci_odp_tds_opendap_test = '
            'ceda.cci_odp_ops_tests.nagios_test.tds_opendap_test:main',
        ],
    },
    zip_safe = False
)
