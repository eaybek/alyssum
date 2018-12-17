import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alyssum",
    version="0.0.11",
    author="Erdem Aybek",
    author_email="eaybek@gmail.com",
    description="A small helper package for personal needs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eaybek/alyssum",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'termcolor',
    ],
)
