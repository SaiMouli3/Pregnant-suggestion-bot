"""
Setup script for MamaCare Assistant.
"""
import os
import sys
from setuptools import setup, find_packages

# Read the README.md for the long description
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Get the version from the package
version = {}
with open(os.path.join('mamacare', '__init__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), version)

setup(
    name='mamacare',
    version=version.get('__version__', '1.0.0'),
    description='A personalized pregnancy support chatbot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/mamacare',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask>=2.3.3',
        'Flask-CORS>=4.0.0',
        'langchain>=0.1.0',
        'langgraph>=0.0.10',
        'google-generativeai>=0.3.0',
        'python-dotenv>=1.0.0',
        'apscheduler>=3.10.1',
        'python-dateutil>=2.8.2',
        'pytz>=2023.3',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.7.0',
            'flake8>=6.1.0',
            'isort>=5.12.0',
            'mypy>=1.5.1',
            'Sphinx>=7.0.1',
            'sphinx-rtd-theme>=1.2.2',
        ],
        'production': [
            'waitress>=2.1.2',
            'gunicorn>=21.2.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'mamacare=mamacare.run:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    python_requires='>=3.8',
)
