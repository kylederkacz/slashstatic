from distutils.core import setup

setup(
    name='slashstatic',
    version='0.1.2',
    description='A library of common static assets in a Django application.',
    author='Kyle Derkacz',
    author_email='slashstatic@kylederkacz.com',
    url='https://github.com/kylederkacz/slashstatic.git',
    data_files=[
        'README.md',
        'CHANGELOG.md',
    ],
    packages=['slashstatic'],
)
