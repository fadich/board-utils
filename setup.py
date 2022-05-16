import os

from setuptools import setup, find_packages


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name='board_utils',
    version='1.0.0-dev',
    keywords=['board', 'board-utils', 'dice', 'games', 'board-games', 'gurps'],
    url='https://github.com/fadich/board-utils',
    author='Fadi A.',
    author_email='royalfadich@gmail.com',
    description='Utilities for board games.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    requires=[
    ],
    scripts=[
    ]
)
