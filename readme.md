# Django Project tsystems

## activate environment

    source .envs/eventenv/bin/activate

## Install project

    pip install pip-tools
    pip-compile requirements.in
    pip-compile requirements-dev.in
    pip-sync requirements.txt requirements-dev.txt

## pip-compile creates:

    requirements.txt 
    requirements-dev.txt

## Create migration files and migrate them (create db table)

    python manage.py makemigrations events
    python manage.py migrate

## Start dev server

    python manage.py runserver


# a little training project

Create new project company_manager
setup .envs/companyenv
setup requirements.in 
pip install pip-tools 
pip-compile requirements.in 
pip-sync requirements.in
create an app company
create a model Company