import subprocess
import os
import tempfile

def install_python():
    """
    Installs python 3.8 and required packages
		
    Args:
    	null
		
    Returns:
        null
    """
    commands = [
    "python3 --version",
    "sudo dpkg --configure -a",
    "sudo apt install software-properties-common -y",
    "yes '' | sudo add-apt-repository ppa:deadsnakes/ppa",
    "sudo apt update -y",
    "sudo apt install -y python3.8",
    "sudo apt update -y",
    "sudo apt-get install python3.8-dev -y",
    "sudo apt update -y",
    "sudo apt install -y python3.8-venv",
    ]
    
    for cmd in commands:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, executable='/bin/bash')
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print(f"Command succeeded: {cmd}\nOutput:\n{stdout.decode('utf-8')}")
        else:
            print(f"Command failed: {cmd}\nError:\n{stderr.decode('utf-8')}")



def create_env(env_name = 'hackathon', parent_of_all_evils_folder = os.getcwd()):
    """
    Creates a virtual environment 
	 
    Args:
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default: os.getcwd()
	 
    Returns:
        os.getcwd()
    """
    if not os.path.exists(parent_of_all_evils_folder):
        os.makedirs(parent_of_all_evils_folder)
    os.chdir(parent_of_all_evils_folder)
    command = f'python3.8 -m venv {env_name}'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Virtual environment '{env_name}' created successfully in parent_of_all_evils_folder: {os.getcwd()}.")
        return os.getcwd()
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment '{env_name}'. Error: {e}")


def run_in_env(command, env_name = 'hackathon',parent_of_all_evils_folder = os.getcwd()):
    """
    Run OS commands for the venv specified. Prints cwd and output of the command.
	 
    Args:
        command (string): OS command to be run
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default: os.getcwd()
	 
    Returns:
        null
    """
    print("cwd:")
    current_dir = os.getcwd()
    full_command = f'cd {parent_of_all_evils_folder} && source ./{env_name}/bin/activate && cd {current_dir} && pwd && {command}'
    process = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, executable='/bin/bash')

    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(f"{output.strip().decode('utf-8')}")
    rc = process.poll()

    if process.stderr is not None:
        for line in process.stderr:
            print('ERROR: ', line.decode('utf-8'), end='')

def run_python_in_env(python_code, env_name = 'hackathon',parent_of_all_evils_folder = os.getcwd()):
    """
    Write python 3.8 command for the venv specified. Prints cwd and output of the program.
	 
    Args:
        command (string): OS command to be run
        env_name (string): the name of the venv, default: 'hackathon'
        parent_of_all_evils_folder (string): the name of the parent folder of the venv, default cwd, default: os.getcwd()
	 
    Returns:
        null
    """
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False, mode='w') as temp:
        temp.write(python_code)
        temp_filename = temp.name

    run_in_env(f'python3 {temp_filename}', env_name, parent_of_all_evils_folder)
    os.remove(temp_filename)