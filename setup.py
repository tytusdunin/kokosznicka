from distutils.core import setup
setup(
  name = 'kokosznicka',
  packages = ['kokosznicka'],
  version = '0.1.3',
  license='GPL-3.0',
  description = 'A simple and effective syllabificator for the Polish language.',
  author = 'Tytus Dunin',
  author_email = 'tm.dunin@student.uw.edu.pl',
  url = 'https://github.com/tytusdunin/kokosznicka',
  download_url = 'https://github.com/tytusdunin/kokosznicka/archive/refs/tags/v.0.1.3.tar.gz',
  keywords = ['nlp', 'syllabification', 'hyphenation', 'polish'],
  install_requires=[],

  classifiers=[
    'Development Status :: 4 - Beta',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)