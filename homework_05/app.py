"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import (
    Flask, # шаблонизатор
    render_template,
    url_for,
    escape,
)
# для работы с шаблонами flask нужен модуль Jinja

app = Flask(__name__)

# - создайте index view `/`
@app.route("/")
def index():
    return render_template('index.html', title="/")

# - добавьте страницу `/about/`, добавьте туда текст
@app.route("/about/")
def about():
    return render_template('about.html', title="/about/")

# # в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
# @app.route('/user/<username>')

# https://flask.palletsprojects.com/en/2.0.x/quickstart/#url-building
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# ===================================================
# @app.route('/')
# @app.route('/about/')
# def index():
#     return 'you are in the index page'
#
# <a href={{ url_for('index') }}>Index</a>

# ===================================================
# with app.test_request_context():
#     print(url_for('/'))
#     print(url_for('/about/'))


# - добавьте новые зависимости в файл `requirements.txt` в корне проекта
#   (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте,
#   что туда попало, и удалите лишнее)


if __name__ == "__main__":
    app.run(debug=True)