import setuptools

from intercom import __version__

with open('README.rst') as readme:
    long_description = readme.read()

setuptools.setup(
    name="intercom",
    version=__version__,
    author="Dimosthenis Schizas",
    author_email="dimos@hackthebox.eu",
    description="Intercom API Python wrapper",
    long_description=long_description,
    url="https://github.com/dimoschi/python-intercom",
    keywords='Intercom CRM Python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    package_dir={"": "intercom"},
    packages=setuptools.find_packages(where="intercom"),
    python_requires=">=3.8",
)
