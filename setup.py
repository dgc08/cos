import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cos-sys",
    version="1.0.2.1",
    description="OS-extension",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dgc08/cos",
    author="DGC-08",
    author_email="digc0820@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cos_sys"],
    include_package_data=True,
    install_requires=[],
)