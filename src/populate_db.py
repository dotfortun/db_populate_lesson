import csv

from flask_sqlalchemy import SQLAlchemy
from main import app, db
from models import User

users = []

with open('src/users.csv', 'rt') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

with app.app_context():
    for user in users:
        db.session.add(user)
    db.session.commit()