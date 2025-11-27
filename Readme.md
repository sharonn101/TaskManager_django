Django Task Manager App

A simple beginner-friendly Task Manager built using Django 5, created as part of the Moringa School AI Capstone Project.

## Features
- Add tasks
- Mark tasks as complete
- Delete tasks
- Minimal, clean UI
- Fully Django-powered (views, models, templates)

## Requirements
- Python 3.12+
- Pipenv
- Django 5.2.8

## Setup Instructions

```bash
pipenv install
pipenv shell
pipenv install django
Create project + app:

bash
Copy code
django-admin startproject taskmanager .
python manage.py startapp tasks
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start server:

bash
Copy code
python manage.py runserver
Open in browser:
http://127.0.0.1:8000/

Project Structure
arduino
Copy code
taskmanager/
  ├── tasks/
  ├── templates/
  │     └── home.html
  ├── taskmanager/
Generated With
This project was built using AI-driven prompts to accelerate learning and debugging.

License
MIT License

yaml
Copy code

---

# 🎉 **You’re done!**