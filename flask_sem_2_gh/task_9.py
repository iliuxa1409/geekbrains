"""
Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        username = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('greetings')))
        response.set_cookie('username', username)
        response.set_cookie('email', email)
        return response
    return render_template('name_email.html')


@app.route('/greetings')
def greetings():
    username = request.cookies.get('username')
    return render_template('greetings.html', name=username)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('name')))
    response.delete_cookie('username')
    response.delete_cookie('email')
    return redirect(url_for('name'))


if __name__ == '__main__':
    app.run(debug=True)
