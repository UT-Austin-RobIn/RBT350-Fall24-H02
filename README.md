# RBT350-Fall24-H02

### Prerequisites
* OS: Mac / Linux / Windows
* Python
* Git

### Seup the codebase
```
git clone https://github.com/UT-Austin-RobIn/RBT350-Fall24-H02.git
cd RBT350-Fall24-H02
```

### Conda environment setup
Check if you already have conda. Type "conda" on the terminal and you should see an output similar to following:
```
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean             Remove unused packages and caches.
    compare           Compare packages between conda environments.
    config            Modify configuration values in .condarc. This is modeled after the git config command. Writes to the user .condarc file
                      (/Users/arpit/.condarc) by default. Use the --show-sources flag to display all identified configuration locations on your
                      computer.
    create            Create a new conda environment from a list of specified packages.
    info              Display information about current conda install.
    init              Initialize conda for shell interaction.
    install           Installs a list of packages into a specified conda environment.
    list              List installed packages in a conda environment.
    package           Low-level conda package utility. (EXPERIMENTAL)
    remove (uninstall)
                      Remove a list of packages from a specified conda environment.
    rename            Renames an existing environment.
    run               Run an executable in a conda environment.
    search            Search for packages and display associated information.The input is a MatchSpec, a query language for conda packages. See
                      examples below.
    update (upgrade)  Updates conda packages to the latest compatible version.
    notices           Retrieves latest channel notifications.

options:
  -h, --help          Show this help message and exit.
  -V, --version       Show the conda version number and exit.

conda commands available from other packages (legacy):
  env
```

If you did not get an output similar to the above, install miniconda through [this link](https://docs.anaconda.com/miniconda/#quick-command-line-install). Once that's done, create a conda environment for the project by running the terminal commands below. If you're on Windows, you will need to do this in the Anaconda Prompt Terminal. Those on Linux and MacOS can run the commands in a regular terminal. 

```
conda create -n rbt350_ho2 python=3.8
conda activate rbt350_ho2
pip install -e .
```

### Running the code
```
python run_robot.py
```
