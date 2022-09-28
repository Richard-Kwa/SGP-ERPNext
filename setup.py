from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sgv/__init__.py
from sgv import __version__ as version

setup(
	name="sgv",
	version=version,
	description="Singapore Version",
	author="Richard Kwa",
	author_email="kwaseng50@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
