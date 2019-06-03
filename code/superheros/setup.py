from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(  name='superheros',
        version=1.0,
        author='Jack Betteridge',
        author_email='jdb55@bath.ac.uk',
        description='',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://arc-lessons.github.io/libraries-modules/00_schedule.html',
        py_modules=['superhero',
                    'superhero2',
                    'check_superheros'
                    ],
        classifiers=[   'Programming Language :: Python :: 3',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: POSIX :: Linux'
                    ]
        )
