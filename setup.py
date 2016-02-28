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


version = '0.0.1'
# version=regatta.__version__,
long_description = open('README.md', 'r').read()

setup(
    name='regatta',
    version=version,
    license='General Public License',
    author='Fabian Sturm',
    author_email='f@rtfs.org',
    url='http://github.com/sturmf/regatta/',
    description='A simple sailing race scoring program.',
    long_description=long_description,
    setup_requires=['flake8'],
    # install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    packages=['regatta'],
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: X11 Applications :: Qt',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        ],
)
