"""
Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""

from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/number', methods=['GET', 'POST'])
def number():
    if request.method == 'POST':
        num = request.form.get('num')
        sq_num = str(int(num) ** 2)
        return render_template('number_res.html', num=num, sq_num=sq_num)
    return render_template('number.html')


if __name__ == '__main__':
    app.run(debug=True)
