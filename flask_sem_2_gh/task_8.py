"""
Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        name_gr = request.form.get('name')
        return render_template('hello_name.html', name=name_gr)
    return render_template('name.html')


if __name__ == '__main__':
    app.run(debug=True)
