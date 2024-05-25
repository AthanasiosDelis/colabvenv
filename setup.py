from setuptools import setup, find_packages

setup(
    name='colabvenv',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={},
    author='Athanasios Delis, Stylianos Kandylakis',
    author_email='athanasiosdelis@gmail.com, stelkcand@gmail.com',
    description='A package that creates python 3.8 virtual environments on Google  Colab and Jupyter Notebooks in Linux OS or WSL Systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/athasdelis/colabvenv',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ],
    python_requires='>=3.6',
)
