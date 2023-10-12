from models import User, db, DEFAULT_IMAGE_URL
from app import app


def seed_db():
    db.drop_all()
    db.create_all()

    User.query.delete()

    # Add users

    john = User(first_name='John', last_name='Doe', image_url= DEFAULT_IMAGE_URL)
    jane = User(first_name='Jane', last_name='Doe', image_url= DEFAULT_IMAGE_URL)
    moonrock = User(first_name='Ryan', last_name='Stivey', image_url= DEFAULT_IMAGE_URL)

    db.session.add(john)
    db.session.add(jane)
    db.session.add(moonrock)

    db.session.commit()

if __name__ == '__main__':
    seed_db()