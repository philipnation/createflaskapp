import os
import sys

def install_flask():
    os.system('pip install flask')
    os.system('pip install flask-sqlalchemy')
    os.system('pip install virtualenv')
    os.system('virtualenv env')
    
    #If you want to start the virtual env
    #################################
    #
    #if sys.platform.startswith('win'):
    #    os.system("env\\Scripts\\activate")
    #elif sys.platform.startswith('linux'):
    #    os.system('source env/bin/activate')
    #elif sys.platform.startswith('darwin'):
    #    print("source env/bin/activate")
    #else:
    #    print("Unknown operating system")
    #    print("virtual env cannot be activated.")
    #    exit()
    #
    ####################################

def create_template_folder():
    try:
        template_folder = "templates"
        template_path = ""
        template_folder_path = os.path.join(template_path, template_folder)
        os.makedirs(template_folder_path)
    except FileExistsError:
        print('folder template exits')
        exit()

def create_static_folder():
    try:
        static_folder = "static"
        static_path = ""
        static_folder_path = os.path.join(static_path, static_folder)
        os.makedirs(static_folder_path)

        # make css folder
        static_folder = "css"
        static_path = "static"
        static_folder_path = os.path.join(static_path, static_folder)
        os.makedirs(static_folder_path)

        # make js folder
        static_folder = "js"
        static_path = "static"
        static_folder_path = os.path.join(static_path, static_folder)
        os.makedirs(static_folder_path)
    except FileExistsError:
        print("folder static already exist")
        exit()


def create_base_file():
    css_file = open("templates/base.html", "a")
    css_file.write('''
<html>
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
        <script src="{{ url_for('static', filename='js/script.js') }}"></script>
        <title>{% block title %}{% endblock title %}</title>
    </head>
    <body>
        {% block body %}{% endblock body %}
    </body>
</html>
    ''')



def create_css_file():
    css_file = open("static/css/style.css", "a")
    css_file.write('''/*
    Write your css style here
*/
    ''')


def create_js_file():
    css_file = open("static/js/script.js", "a")
    css_file.write('''//write your js script here
    ''')

def create_index_file():
    css_file = open("templates/index.html", "a")
    css_file.write('''
{% extends 'base.html' %}
{% block title %}home{% endblock title %}
{% block body %}
<h1 style="color: green">This is the home page</h1>
{% endblock body %}
    ''')

def create_about_file():
    css_file = open("templates/about.html", "a")
    css_file.write('''
{% extends 'base.html' %}
{% block title %}home{% endblock title %}
{% block body %}
<h1 style="color: green">This is the about page</h1>
{% endblock body %}
    ''')


def create_readme():
    css_file = open("readme.md", "a")
    css_file.write('''## Flask start app automated by philip nation
# tictok handle @your_programmer

## The basic functions
This script checks for the presence of Flask, virtual environment, and SQLAlchemy on your system, and installs them if they are not already present. This ensures that you have all the necessary dependencies installed for your Python Flask project.

## start flask app
This Python script automates the creation of basic files required to start a Flask application. Running the createapp.py script generates a template folder, a static folder, and the base.html, index.html, style.css, and script.js files in their respective folders. This saves time and ensures that the necessary files are created in the correct locations.

## start the app
Finally, the script executes the app.py script that it created to launch the Flask application. This starts the server and allows you to view the application in a web browser.''')


def create_app():
    mainapp = open("app.py", "a")
    mainapp.write('''from flask import Flask, render_template, url_for,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)''')


def start_app():
    os.system("python app.py")
    os.remove('createapp.py')
    os.remove('setup.py')


def create_flask_app():
    install_flask()
    create_template_folder()
    create_static_folder()
    create_css_file()
    create_js_file()
    create_index_file()
    create_base_file()
    create_about_file()
    create_readme()
    create_app()
    start_app()