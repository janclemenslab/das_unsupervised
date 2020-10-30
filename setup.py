from setuptools import setup, find_packages
import codecs
import re
import os

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# read the contents of the README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='dss_unsupervised',
      version=find_version("src/deepss_unsupervised/__init__.py"),
      description='deepsongsegmenter unsupervised',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/janclemenslab/deess-unsupervised',
      author='Jan Clemens',
      author_email='clemensjan@googlemail.com',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['numpy', 'scipy', 'sklearn',
                        'matplotlib', 'colorcet', 'seaborn',
                        'librosa', 'noisereduce', 'Pillow',
                        'umap-learn', 'hdbscan'],
      include_package_data=True,
      zip_safe=False,
     )
