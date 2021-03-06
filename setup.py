from setuptools import setup
from reportermd.cli import __VERSION__

setup(
    name='reportermd',
    packages=['reportermd'],
    version=__VERSION__,
    description='Convert your Reporter App dates to MD then import to Day One',
    author='Sam Beveridge',
    author_email='sam.bev87@gmail.com',
    license='MIT',
    url='https://github.com/sambev/reportermd',
    entry_points={
        'console_scripts': [
            'reportermd=reportermd.cli:main',
        ]
    },
    include_package_data=True,
    install_requires=[
        'Jinja2>=2.8',
        'python-dateutil==2.4.2',
    ]
)
