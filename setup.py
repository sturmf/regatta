import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='regatta',
    #version=regatta.__version__,
    version='0.0.1',
    url='http://github.com/sturmf/regatta/',
    license='General Public License',
    author='Fabian Sturm',
    tests_require=['pytest'],
    #install_requires=[],
    cmdclass={'test': PyTest},
    author_email='f@rtfs.org',
    description='A simple sailing race scoring program.',
    #long_description=long_description,
    packages=['regatta'],
    #include_package_data=True,
    platforms='any',
    #test_suite='sandman.test.test_sandman',
    #classifiers = [
    #    'Programming Language :: Python',
    #    'Development Status :: 4 - Beta',
    #    'Natural Language :: English',
    #    'Environment :: Web Environment',
    #    'Intended Audience :: Developers',
    #    'License :: OSI Approved :: Apache Software License',
    #    'Operating System :: OS Independent',
    #    'Topic :: Software Development :: Libraries :: Python Modules',
    #    'Topic :: Software Development :: Libraries :: Application Frameworks',
    #    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    #    ],
    extras_require={
        'testing': ['pytest'],
    }
)
