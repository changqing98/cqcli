import io
import os
import setuptools

name = '${name}'
version = '${version}'
description = 'gRPC library for ${name}'
package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, 'README.rst')
with io.open(readme_filename, encoding='utf-8') as readme_file:
  readme = readme_file.read()

dependencies = [
    'googleapis-common-protos >= 1.6.0',
]

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Internet',
    ],
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    zip_safe=False,
)
