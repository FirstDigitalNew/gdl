import re

from setuptools import find_packages
from setuptools import setup


version = "6.0.0"


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()

    try:
        import github2pypi  # NOQA

        return github2pypi.replace_url(
            slug="Chitranjan6G/gdl", content=long_description
        )
    except Exception:
        return long_description


setup(
    name="gdl",
    version=version,
    packages=find_packages(exclude=["github2pypi"]),
    install_requires=[
        "filelock",
        "requests[socks]",
        "six",
        "tqdm",
        "beautifulsoup4",
    ],
    description="Google Drive direct download of big files.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Chitranjan6G",
    author_email="chitranjanmahto78@gmail.com",
    url="http://github.com/Chitranjan6G/gdl",
    license="MIT",
    keywords="Data Download",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": ["gdl=gdl.cli:main"]},
)
