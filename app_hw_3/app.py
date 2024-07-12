from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from forms import RegisterForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Welcome to the site!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )
        new_user.set_password(password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration Complete', 'success')
        return render_template('register.html', form=form, success=True)
    return render_template('register.html', form=form, success=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
