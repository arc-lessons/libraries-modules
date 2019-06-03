import setuptools

# Long description comes from README file
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='libraries-modules',
    version='1.0',
    author='James Grant, Jack Betteridge',
    packages=setuptools.find_packages(),
    package_dir = {'': 'code'},
    #package_data={},
    #include_package_data=True,
    py_modules=['superhero', 'superhero2', 'morse_answer'],
    #install_requires = [],
    #entry_points={},
    author_email='rjg20@Bath.ac.uk',
    description='Modules required for the lesson libraries-modules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/arc-lessons/libraries-modules',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
    ],
)
