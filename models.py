from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    file = db.Column(db.Text, nullable=True)

    photo_url = db.Column(db.Text, default="https://lastchanceatlife.org/wp-content/uploads/2018/06/Last_Chance_At_Life_Pet_Adoption_Coming-Soon.jpg", nullable=True)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)

    @classmethod
    def get_available_pets(cls):
        return cls.query.filter(cls.available == True).order_by(func.lower(cls.species), func.lower(cls.name)).all()

    @classmethod
    def get_unavailable_pets(cls):
        return cls.query.filter(cls.available == False).order_by(func.lower(cls.species), func.lower(cls.name)).all()