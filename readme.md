# Django Project tsystems

## create environment

    python -m venv .envs/enventenv

## activate environment

    source .envs/eventenv/bin/activate

## Install project

    (eventenv) pip install pip-tools
    (eventenv) pip-compile requirements.in
    (eventenv) pip-compile requirements-dev.in
    (eventenv) pip-sync requirements.txt requirements-dev.txt

## pip-compile creates:

    requirements.txt 
    requirements-dev.txt

## Create migration files and migrate them (create db table)

    (eventenv) python manage.py makemigrations events
    (eventenv) python manage.py migrate

## Start dev server

    (eventenv) python manage.py runserver

## Docs

    https://docs.djangoproject.com/en/4.2/
    https://github.com/jazzband/pip-tools
    https://miro.medium.com/v2/resize:fit:700/1*aICZBUzrgLgc5GoWuiFHcw.jpeg
    https://github.com/cookiecutter/cookiecutter-django



# a little training project

Create new project company_manager
setup .envs/companyenv
setup requirements.in 
pip install pip-tools 
pip-compile requirements.in 
pip-sync requirements.in
create an app company
create a model Company