from setuptools import find_packages, setup

with open("calfacto/README.md", "r") as f:
    long_description = f.read()

setup(
    name="calfacto",
    version="0.0.4",
    description="Calculate factorial of a number",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Subhajit Guha Thakurta",
    author_email="subhajitguha79@gmail.com",
    license="MIT",
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)