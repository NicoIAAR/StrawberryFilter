from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='ContadorDeS',
    packages=['ContadorDeS'],  # this must be the same as the name above
    version='0.1',
    description='Cuenta las veces que aparece la letra s en un texto',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Nico',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/NicoIAAR',
    download_url='https://github.com/NicoIAAR/StrawberryFilter',
    keywords=['strawberry', 'python', 'pip'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)