"""
Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from pathlib import Path, PurePath
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.get('/')
def index_get():
    return render_template('contact.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_name = secure_filename(file.filename)
            save_directory = Path.cwd() / 'uploads'
            save_directory.mkdir(parents=True, exist_ok=True)
            file.save(save_directory / file_name)
            save_path = PurePath.joinpath(Path.cwd(), 'uploads', file_name)
            print('Saved in: ', save_path)
            return f'File {file_name} was uploaded'

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
