
# list enviorment
conda info --envs

# remove enviorment
conda remove --name myenv --all

conda create --name myDjangoENV django

conda activate myDjangoENV


django-admin startproject first_project


# notice that these are different
python manage.py startapp first_app

python manage.py runserver
