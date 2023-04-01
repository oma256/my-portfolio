import locale
from datetime import datetime, timedelta
import smtplib

from flask import Flask, render_template

from models import db, User, Position, Skill, Resume, Summary, Education
from utils import init_app

app = Flask(__name__)
app.config.from_object('settings')
init_app(app=app)
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


@app.route('/')
def index():
    user = db.session.query(User).first()
    position = db.session.query(Position).filter_by(user_id=user.id).first()
    skills = db.session.query(Skill).filter_by(position_id=position.id).all()
    resume = db.session.query(Resume).filter_by(position_id=position.id).first()
    summary = db.session.query(Summary).filter_by(resume_id=resume.id).first()
    educations = db.session.query(Education).filter_by(resume_id=resume.id).all()

    user_info = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth,
        'age': datetime.today().date().year - user.date_of_birth.year,
        'phone_number': user.phone_number,
        'address': user.address,
        'email': user.email,
        'position': {
            'name': position.name,
            'description': position.description,
            'freelance': position.freelance,
            'skills': skills,
            'resume': {
                'description': resume.description,
                'summary': summary,
                'educations': educations,
            }
        }
    }

    return render_template('index.html', user_info=user_info)


@app.route('/send-mail')
def send_mail():
    smtp_server = "smtp.elasticemail.com"
    port = 2525
    username = "your_username"
    password = "your_password"

    from_email = "you@example.com"
    to_email = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent via ElasticEmail and Python 3"

    message = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}"
    try:
        smtpObj = smtplib.SMTP(smtp_server, port)
        smtpObj.login(username, password)
        smtpObj.sendmail(from_email, to_email, message)
        print("Email sent successfully")
    except Exception as e:
        print("Error: unable to send email")
        print(e)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
