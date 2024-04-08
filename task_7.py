"""
Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    news = [
        {
            'title': 'Hey yo',
            'description': 'Something about greetings',
            'date': '20/11/2023'
        },
        {
            'title': 'First book',
            'description': 'First book is published',
            'date': '30/10/1616'
        },
        {
            'title': 'Anytime, Anywhere',
            'description': 'almighty bush',
            'date': '11/05/2000'
        }
    ]
    context = {
        'articles': news
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
