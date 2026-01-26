"""
Setup script for the Data Science course utilities.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="data-science-henry",
    version="1.0.0",
    author="Mariano Gobea",
    author_email="mariano.gobea@mercadolibre.com",
    description="Curso completo de Data Science y Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/data-science-henry",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
    ],
)
