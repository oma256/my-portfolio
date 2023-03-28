import locale
from datetime import datetime, timedelta

from flask import Flask, render_template

from models import db, User, Position
from utils import init_app

app = Flask(__name__)
app.config.from_object('settings')
init_app(app=app)
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


@app.route('/')
def index():
    user = db.session.query(User).first()
    position = db.session.query(Position).filter_by(user_id=user.id).first()

    user_info = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
        'age': datetime.today().date().year - user.date_of_birth.year,
        'phone_number': user.phone_number,
        'address': user.address,
        'position': {
            'name': position.name,
            'description': position.description,
        }
    }

    return render_template('index.html', user_info=user_info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
