#!/usr/bin/env python
import subprocess
import sys

venv_env_creation = True if "{{ cookiecutter.create_python_venv }}" == "Yes" else False
init_git = True if "{{ cookiecutter.init_git }}" == "Yes" else False

if venv_env_creation:
    try:
        subprocess.run(["make", "init_venv"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)

if init_git:
    try:
        subprocess.run(["make", "init_git"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)
