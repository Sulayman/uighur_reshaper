from pathlib import Path

from setuptools import find_packages, setup

LONG_DESCRIPTION = Path(__file__).parent.joinpath("README.md").read_text(encoding="utf-8")

setup(
    name="uighur_reshaper",
    version="0.2.0",
    author="Sulayman",
    author_email="Sulayman@eotor.net",
    description="A Python tool for reshaping Uyghur text between the basic Arabic block and Arabic Presentation Forms.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Sulayman/uighur_reshaper",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: Other",
    ],
    keywords="uyghur uighur arabic reshape presentation-forms text",
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "uighur_reshaper=uighur_reshaper.shaper:main",
        ],
    },
)
