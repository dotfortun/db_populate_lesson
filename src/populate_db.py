import csv, json

from main import app, db
from models import Lesson

from tqdm import tqdm

lessons = None
lesson_objs = []

with open("src/lessons.json", 'rt') as json_file:
    data = json.load(json_file)
    lessons = data

with app.app_context():
    """{
        "word": "hello",
        "phonetic": "həˈlō",
        "mandarin": "你好",
        "phoneticM": "Nǐ hǎo",
        "images": "as",
        "part_of_speech": "as"
    }"""
    for lesson in lessons:
        lesson_objs.append(Lesson(
            word=lesson["word"],
            phonetic=lesson["phonetic"],
            mandarin=lesson["mandarin"],
            phoneticM=lesson["phoneticM"],
            images=lesson["images"],
            part_of_speech=lesson["part_of_speech"],
        ))
    db.session.add_all(lesson_objs)
    db.session.commit()

# users = []

# with open('src/users.csv', 'rt') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in tqdm(reader):
#         u = User(
#             email=row['email'],
#             username=row['login/username'],
#             password=row['login/password'],
#             title=row['name/title'],
#             first_name=row['name/first'],
#             last_name=row['name/last'],
#             phone=row['phone'],
#             is_active=True,
#         )
#         users.append(u)

# with app.app_context():
#     for user in tqdm(users):
#         db.session.add(user)
#     db.session.commit()