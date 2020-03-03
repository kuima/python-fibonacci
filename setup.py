from setuptools import find_packages, setup

setup(
    name='fibonacci',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fibonacci = fibonacci.bin:compute'
        ]
    }
)
