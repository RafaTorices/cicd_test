from setuptools import setup, find_packages

setup(
    name="calculator",
    version="1.0.3",
    author="RafaelTorices",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
    ],
    entry_points={
        "console_scripts": [
            "calculator=src.calculator:app.run",
        ],
    },
    package_data={
        "calculator": ["templates/*.html"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
