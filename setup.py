import setuptools

setuptools.setup(
    name='adht',
    version='0.1',
    package_dir={'': 'adht'},
    requires=[i.strip() for i in open('requirements.txt', 'r').read().split('\n') if i.strip() is not '']
)
