#!/usr/bin/env python

from os import path
from io import open
from setuptools import setup, find_packages
from logging_azure import get_version

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
    setup(
        name="logging-azure-rest",
        version=get_version(),
        description="A python threadded logging handler and service extension for Azure Log Workspace OMS REST API.",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Joshua Logan",
        author_email="joshua.logan@exelscior.eu",
        url="https://github.com/Exelscior/logging-azure-rest",
        packages=find_packages(),
        license="MIT",
        keywords="utils",
        python_requires=">=3.7",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Plugins",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        install_requires=["injector>=0.18.4", "requests>=2.25.1", "dataclasses-json>=0.5.2"],
    )
