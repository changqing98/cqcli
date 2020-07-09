import os

from setuptools import setup, find_packages

# read requirement.txt
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = [_.strip() for _ in f.readlines() if not _.startswith('#')]

setup(
    name="cqcli",
    author="changqing",
    author_email="yecq1998@outlook.com",
    version="1.0.1",
    install_requires=requirements,
    packages=find_packages()
)
