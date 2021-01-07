from setuptools import setup

setup(
    name="SV-Switch",
    version="0.0.0",
    description="A runit service manager",
    url="https://github.com/Bikutoso/sv-switch",
    author="Bikutoso",
    license="ICS",
    packages=["svs"],

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Topic :: System :: Boot :: Init",
    ],
)
