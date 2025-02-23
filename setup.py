#!/usr/bin/env python


"""Set up the cobra package."""
from setuptools import setup


# All other arguments are defined in `setup.cfg`.
if __name__ == "__main__":
    setup(
        version='2.0.8',
        entry_points={
            "console_scripts": [
            'chimera=src.ChiMera.chimera_core:main',
        ]
    }
    )        
