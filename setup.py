# setup.py
from setuptools import setup, find_packages

setup(
    name='whichY',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'biopython',  
        'pysam',
        'pyfaidx',
        'ytree',
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'whichY=whichY.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
