from setuptools import setup

NAME = "Lunodin"
DESCRIPTION = "Открытый и бесплатный СМС бомбер 💣"
URL = "https://github.com/lunodin/Lunodin"
EMAIL = ""
AUTHOR = "lunodin"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "2.5.8.1"

REQUIRED = ["aiohttp", "aiodns", "phonenumbers", "click", "sentry-sdk"]

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["Lunodin"],
    entry_points={
        "console_scripts": ["Lunodin=Lunodin.__main__:main", "lunodin=Lunodin.__main__:main",]
    },
    install_requires=REQUIRED,
    extras_require={},
    package_data={"Lunodin": ["static/*/*", "templates/*", "services/*"]},
    license="Mozilla Public License 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
)
