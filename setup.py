import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('VERSION', 'r') as fh:
    version = fh.read().strip()

setuptools.setup(name='pyhepevt',
                 version=version,
                 description='A package to help interface with the HepEvt format',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 author='Peter Madigan',
                 author_email='pmadigan@berkeley.edu',
                 package_dir={'': '.'},
                 packages=setuptools.find_packages(where='.'),
                 python_requires='>=3.7',
                 )
