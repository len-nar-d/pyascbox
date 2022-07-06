from distutils.core import setup

setup(
  name = 'pyascbox',
  packages = ['pyascbox'],
  version = '0.1',
  license='MIT',
  description = 'Creates an ascii box around a string with head and body.',
  author = 'Lennard Spors',
  author_email = 'lennard.spors@gmail.com',
  url = 'https://github.com/len-nar-d/pyascbox',
  download_url = 'https://github.com/len-nar-d/pyascbox/archive/refs/tags/v0.1.tar.gz',
  keywords = ['box', 'asciibox'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)