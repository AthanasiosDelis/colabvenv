# colabvenv

A package that creates python 3.8 virtual environments on Google  Colab and Jupyter Notebooks in Linux OS or WSL Systems.

## Installation

pypi package:

```bash
pip install colabvenv
```

wheel package:

```
pip install colabvenv-0.1-py3-none-any.whl
```

## Import

```
from colabvenv import install_python, create_env, run_in_env, run_python_in_env
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
```

```
create_env(env_name, parent_of_all_evils_folder):
    """
    Creates a virtual environment 
	 
    Args:
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default: os.getcwd()
	 
    Returns:
        os.getcwd()
    """
```

```
run_in_env(command, env_name, parent_of_all_evils_folder):
    """
    Run OS commands for the venv specified. Prints cwd and output of the command.
	 
    Args:
        command (string): OS command to be run
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default: os.getcwd()
	 
    Returns:
        null
    """
```

```
run_python_in_env(command, env_name, parent_of_all_evils_folder):
    """
    Write python 3.8 command for the venv specified. Prints cwd and output of the program.
	 
    Args:
        command (string): OS command to be run
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default cwd, default: os.getcwd()
	 
    Returns:
        null
    """
```
		
## Citation

Copyright (c) 2024 Athanasios, Delis, Stylianos, Kandylakis. Licensed under the MIT License (the "License");

```bibtex
@misc{Athanasios2024,
  author = {Athanasios Delis, Stylianos Kandylakis},
  title = {colabvenv},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/AthanasiosDelis/colabvenv/}}
}
```

## Contributions

Contributions are welcome. Please raise issues as necessary. All issues, as they come up, will be definitely solved to the best of my abilities. Till then if you send a merge request, describe the problem, the fix and why it works.
