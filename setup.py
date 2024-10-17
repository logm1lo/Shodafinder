from setuptools import setup, find_packages

setup(
    name="shodafinder",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "mmh3",
        "favicon",
    ],
    entry_points={
        "console_scripts": [
            "shodafinder=favicon_hash.cli:run",
        ]
    },
    author="Thanh Sang",
    author_email="logmilo12@gmail.com",
    description="A tool to hash favicons for Shodan and ZoomEye searches.",
    url="https://github.com/logm1lo/Shodafinder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

