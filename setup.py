from setuptools import setup, find_packages

setup(
    name='envbuilder',
    version='0.1.0',
    packages=find_packages(),
    setup_requires=['nose'],
    install_requires=['ConfigObj', 'argparse'],
    zip_safe=True,
    entry_points = {
        'console_scripts' : [
            'envbuilder = envbuilder.run:main'
            ]
        }
    )
