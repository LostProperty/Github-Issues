import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='feedback',
      version='0.1.0',
      description='Feedback via github issues',
      long_description=README,
      classifiers=['Private :: Do Not Upload'],
      author='pete@lostpropertyhq.com',
      author_email='pete@lostpropertyhq.com',
      url='feedback.lostpropertyhq.com',
      keywords='',
      package_dir={'': 'feedback'},
      packages=find_packages('feedback'),
      include_package_data=True,
      zip_safe=False,
      )
