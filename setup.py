'''
setup.py - a setup script
Licensed under the MIT License
'''
from setuptools import setup
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='flawunicode',
    version='0.1.2',
    description='detect flaw or encoding error in unicode text',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Ray',
    author_email='ray@currentsapi.services',
    url='https://github.com/currentslab/flawunicode',
    keywords='unicode,detection,annomaly',
    packages=['flawunicode'],
    package_data={'flawunicode': ['flawunicode/*', 'resources/*']},
    include_package_data=True,
    install_requires=[],
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)