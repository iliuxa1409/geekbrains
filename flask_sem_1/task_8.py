"""
Задание №8
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'main'


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
