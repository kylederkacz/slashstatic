from distutils.core import setup

setup(
    name='slashstatic',
    version='0.1.0',
    description='A library of common static assets in a Django application.',
    author='Kyle Derkacz',
    author_email='kyleder@gmail.com',
    url='https://github.com/kylederkacz/slashstatic.git',
    data_files=[
        'README.md',
        'CHANGELOG.md',
    ],
    packages=['slashstatic'],
)
