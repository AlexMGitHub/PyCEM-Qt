from setuptools import setup, find_packages

setup(
    name="pycem-qt",
    packages=find_packages(where="src"),
    package_dir={'': 'src'}
)
