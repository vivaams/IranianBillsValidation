from setuptools import setup, find_packages


setup(
    name="iranian_bills_validation",
    version='0.0.1',
    license='MIT',
    author="Amin Morakabi Sabet",
    author_email="vivaams@yahoo.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url="https://github.com/vivaams/iranian_bills_validation",
    keywords='iranian bills validation',
    install_requires=[
          'jdatetime',
      ],

)