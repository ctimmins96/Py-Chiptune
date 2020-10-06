import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyChiptune-ctimmins96", # Replace with your own username
    version="1.0",
    author="Chase Timmins",
    author_email="git.brackish@gmail.com",
    description="A Python package used to create Chiptune music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctimmins96/Py-Chiptune",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
