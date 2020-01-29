from setuptools import setup, find_packages
import re

version = re.search(
    r'^__VERSION__\s*=\s*"(.*)"', open("freefall/__init__.py").read(), re.M
).group(1)

setup(
    name="freefall",
    version=version,
    packages=find_packages(),
    url="",
    license="MIT",
    author="Chad Stryker",
    author_email="",
    description="A Python package module for simulating falling objects with aerodynamic drag.",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
