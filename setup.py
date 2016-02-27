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
    license='General Public License',
    author='Fabian Sturm',
    author_email='f@rtfs.org',
    url='http://github.com/sturmf/regatta/',
    description='A simple sailing race scoring program.',
    #long_description=long_description,
    #install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    packages=['regatta'],
    platforms='any',
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
)
