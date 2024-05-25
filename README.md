# colabenv

A package that creates a python 3.8 virtual environment on Linux OS ( Colab and Jupyter included ).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         in Google Colab.



## Installation

```bash

pypi package:
pip install colabenv

wheel package:
pip install colabenv_pckg-0.1-py3-none-any.whl
```

## Import

```
from colabenv import install_python, create_env, run_in_env, run_python_in_env
```

## Functions

```
install_python(): 

		"""
		Installs python 3.8 and required packages
		
		Args:
			null
		
		Returns:
			null
		"""

create_env(env_name):

		"""
		Creates a virtual environment 
	 
		Args:
			env_name (string): the name of the venv
	 
		Returns:
			null
		"""

run_in_env(command, env_name):

		"""
		Run OS commands for the venv specified
	 
		Args:
			command (string): OS command to be run
			env_name (string): the name of the venv
	 
		Returns:
			command respond
		"""

run_python_in_env(command, env_name):

		"""
		Write python 3.8 command for the venv specified
	 
		Args:
			command (string): OS command to be run
			env_name (string): the name of the venv
	 
		Returns:
			command respond
		"""
```
		
## Citation

```
Copyright (c) 2024 Athanasios, Delis, Stylianos, Kandylakis. Licensed under the MIT License (the "License");
```

```bibtex
@misc{torchkan,
  author = {Athanasios Delis, Stylianos Kandylakis},
  title = {colabenv},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/AthanasiosDelis/colabenv/}}
}
```

## Contributions

```
Contributions are welcome. Please raise issues as necessary. All issues, as they come up, will be definitely solved to the best of my abilities. Till then if you send a merge request, describe the problem, the fix and why it works.
```
		