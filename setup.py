import os
from setuptools import setup #, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='feedback',
      version='0.1.0',
      packages=['feedback'],
      include_package_data=True,
      description='Feedback via github issues',
      long_description=README,
      url='feedback.lostpropertyhq.com',
      author='pete@lostpropertyhq.com',
      author_email='pete@lostpropertyhq.com',
      keywords='',
      #package_dir={'': 'feedback'},
      zip_safe=False,
      classifiers=['Private :: Do Not Upload'],
)
