## Python Knowledge Assessment Tool
---
### Poetry: create new project in current directory (dir must be empty)

> poetry new --name=PACKAGE_NAME [--src] .

### Poetry: view config

> poetry config --list

### Poetry: create virtual environment in project directory

- configure poetry to create venv in .venv directory under project folder
> poetry config virtualenvs.create true
</br>
> poetry config virtualenvs.in-project true 
</br>
> export POETRY_VIRTUALENVS_IN_PROJECT=true

- create virtual environment in .venv folder by specifying python interpretor
> poetry env use --ansi -vv -- python

- list created virtual environment
> poetry env list

- activate virtual environment if it's not activated 
> . /PROJECT_DIR/.venv/bin/activate

- spawns a shell within the virtual environment
> poetry shell

### Poetry: add new dependency to pyproject.toml file

> poetry add [--group=GROUP] PACKAGE==VERSION
</br>
> poetry show