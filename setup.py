import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lru-cache-lceames", # Replace with your own username
    version="0.0.2",
    author="Lee Eames",
    author_email="lceames@gmail.com",
    description="An efficient LRUCache class leveraging the OrderedDict class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lceames/lru-cache",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)