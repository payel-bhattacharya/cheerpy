from setuptools import setup, find_packages

setup(
    name="cheerpy",  
    version="0.1.0",
    author="Payel Bhattacharya",
    author_email="bhattacharyanina@gmail.com",
    description="A fun library to cheer you up with random success/failure messages in CI/CD pipelines",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/payel-bhattacharya/cheerpy",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
