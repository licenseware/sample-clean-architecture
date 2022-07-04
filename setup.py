from setuptools import find_packages, setup


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="sample-clean-architecture",
    version="0.1.0",
    install_requires=get_requirements(),
    packages=find_packages("."),
)
