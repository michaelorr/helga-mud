import os
from setuptools import setup, find_packages

from helga_mud import __version__ as version

requirements = []
with open(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r'
) as in_:
    requirements = in_.readlines()


setup(
    name="helga-mud",
    version=version,
    description=(''),
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: IRC',
        'Intended Audience :: Twisted Developers, IRC Bot Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: IRC Bots'],
    keywords='irc bot mud',
    author='Michael Orr',
    author_email='michael@orr.co',
    url='https://github.com/michaelorr/helga-mud',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga-mud'],
    zip_safe=True,
    install_requirements=requirements,
    entry_points = dict(
        helga_plugins=[
            'mud = helga_mud.plugin:mud',
        ],
    ),
)
