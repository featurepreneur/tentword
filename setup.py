import os
import re
from setuptools import setup
from setuptools import find_packages


ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)))
VERSION_RE = re.compile(r'''__version__ ?= ?['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(ROOT, 'tentword', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


with open(ROOT + '/README.md', 'r') as fp:
    long_description = fp.read()


setup(
    name='tentword',
    version=get_version(),
    author='Raja CSP Raman',
    author_email='raja.r.csp@gmail.com',
    description='TentWord for Python 3.6+',
    long_description=long_description,
    long_description_content_type='test/markdown',
    url='https://github.com/tactlabs/tentword.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'aiohttp'],
)

