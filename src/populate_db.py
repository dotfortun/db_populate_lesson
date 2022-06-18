import csv

from main import app, db
from models import User

from tqdm import tqdm

users = []

with open('src/users.csv', 'rt') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in tqdm(reader):
        u = User(
            email=row['email'],
            username=row['login/username'],
            password=row['login/password'],
            title=row['name/title'],
            first_name=row['name/first'],
            last_name=row['name/last'],
            phone=row['phone'],
            is_active=True,
        )
        users.append(u)

with app.app_context():
    for user in tqdm(users):
        db.session.add(user)
    db.session.commit()