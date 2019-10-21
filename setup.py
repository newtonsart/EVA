

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EVA",
    version="0.0.1",
    author="LilArt",
    author_email="artsecurity@protonmail.com",
    description="A simple voice assistant called EVA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lilart/EVA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

