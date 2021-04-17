# Python
Python is a multi-purpos and versetile language

## Installing Python
Go to python website to download Latest Python

## Implementation
There are several implementation of Python
* **CPython** : The core is written in C (Default)
* **Jython** : The core is written in Java
* **IronPython** : The core is written in C#
* **PyPy** : The core is written using sunbet of python

## Access to python in terminal
Access to python in terminal can be different. You can use:
* **python**
* **python3**
* **py**

## Installing packages in python
Pip is the python package manager that comes with python
* Install a package/library:
    * '**pip install django**' : install django latest version
    * '**pip install django flask fbs**' : install more than one
    * '**pip install django==2.2 flask**' : install specific version
    * '**pip install -r requirements.txt**' : install all packages defined in requirements.txt file
* Uninstall a package/library:
    * '**pip uninstall django**' : uninstall django latest version
    * '**pip uninstall django flask fbs**' : uninstall more than one
* List of all installed packages :
    * '**pip list**' : Output installed packages
    * '**pip freeze**' : Output installed packages in requirements format
    * '**pip freeze > requirements.txt**' : Write installed packages in requirements.txt file

## Virtual Environment
It is used because defferent versions of a package can be used in defferent projects.
So, just **create a virtual environment**, **install your packages** and **activate venv**.
* Creating a new venv :
    * '**python -m venv tutorial-env**' : Create a venv in tutorial-env (Use 'venv' in 'tutorial-env' to make easier)
* Activating venv :
    * '**tutorial-env\Scripts\activate.bat**' : This command will activate the venv for that terminal
    * In vs code, once venv is detected and selected, everytime the terminal opens, the activating command will be exicuted automaticly
