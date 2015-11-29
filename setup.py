from setuptools import setup

setup(
    name='reportermd',
    packages=['reportermd'],
    version='0.0.1',
    description='Convert your Reporter App dates to MD then import to Day One',
    author='Sam Beveridge',
    author_email='sam.bev87@gmail.com',
    license='MIT',
    url='https://github.com/sambev/reportermd',
    scripts=['bin/reportermd'],
    include_package_data=True,
    install_requires=[
        'Jinja2>=2.8',
        'python-dateutil==2.4.2',
    ]
)
