"""
Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
menu = [{'name': 'Main', 'url': 'index'},
        {'name': 'About', 'url': 'about'},
        {'name': 'Contact', 'url': 'contact'}]


@app.route('/')
def index():
    return render_template('base.html', menu=menu)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greetings', name=name))
    return render_template('contact.html', title='Contact us', menu=menu)


@app.route('/greetings/<name>')
def greetings(name):
    return render_template('greetings.html', title='Greetings', name=name)


if __name__ == '__main__':
    app.run(debug=True)
