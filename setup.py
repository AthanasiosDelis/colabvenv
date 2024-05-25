from setuptools import setup, find_packages

setup(
    name='colabenv',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    author='Athanasios Delis, Stylianos Kandylakis',
    author_email='athanasiosdelis@gmail.com, stelkcand@gmail.com',
    description='A package to create virtual environments of Python3.8 on Google Colab and Jupyter Notebook in Linux or wsl OS systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/athasdelis/colabenv',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
    ],
    python_requires='>=3.6',
)
