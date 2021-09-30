from distutils.core import setup

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='iranian_bills_validation',
    packages=['iranian_bills_validation'],
    version='1.1.2',
    license='MIT',
    description='This module checks and validates your bills and returns the required information',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Amin Morakabi Sabet',
    author_email='vivaams@yahoo.com',
    url='https://github.com/vivaams/iranian_bills_validation',
    project_urls={
        "Bug Tracker": "https://github.com/vivaams/iranian_bills_validation/issues",
    },
    keywords=['bills', 'validation'],
    install_requires=[
            'jdatetime',
        ],
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
)
