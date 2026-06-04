"""
Setup script for the Data Science course utilities.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [
        line.strip()
        for line in f
        if line.strip() and not line.strip().startswith("#")
    ]

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
    install_requires=requirements,
)
