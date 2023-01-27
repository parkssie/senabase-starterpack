from setuptools import setup, find_packages

setup(name='senabase-starterpack',
      version='0.1.1',

      description='SENABASE Starterpack',
      author='Jungkyu Park',
      author_email='parkssie@gmail.com',
      url='https://github.com/parkssie/senabase-starterpack',

      python_requires='>=3.11',
      package_dir={'': 'senabase'},
      packages=find_packages("senabase", exclude=["prototypes"]),
      install_requires=[
          'psycopg2-binary>=2.9.*',
          'pyyaml>=6.*',
      ])
