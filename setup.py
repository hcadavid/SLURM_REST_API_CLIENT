# coding: utf-8

"""
    Slurm Rest API RO

    API to access Slurm. Only GET requests are implemented.

    The version of the OpenAPI document: 0.0.38
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "openapi-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Slurm Rest API RO",
    author="SchedMD LLC",
    author_email="sales@schedmd.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Slurm Rest API RO"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    API to access Slurm. Only GET requests are implemented.
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)
