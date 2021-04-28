import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cos-sys",
    version="1.0.0",
    description="OS-extension",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dgc08/cos",
    author="DGC-08",
    author_email="digc0820 [at] gmail [dot] com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cos-sys"],
    include_package_data=True,
    install_requires=["sys", "os"]
)