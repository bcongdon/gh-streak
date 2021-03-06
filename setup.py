from distutils.core import setup

setup(
  name='ghstreak',
  version='0.1.3',
  description='A Python library for fetching GitHub contribution streaks.',
  author='Christopher Su',
  author_email='chris+py@christopher.su',
  url='https://github.com/csu/gh-streak',
  packages=['ghstreak'],
  install_requires=[
    "requests==2.10.0"
  ],
  entry_points = {
      'console_scripts': ['ghstreak=ghstreak.cli:main'],
  }
)