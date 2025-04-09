from models import db, Pet
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()
    
    milo = Pet(name='Milo', species='Dog', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO5U9u20Sw2CyVVLwAjRYjeraJK14UV0EZ5Q&s', age=1,  notes='very very nice and very handsome', available=False)

    marvin = Pet(name='Marvin', species='Cat', photo_url='https://cdn-useast1.kapwing.com/static/templates/woman-yelling-at-cat-meme-template-thumbnail-7c3091cf.webp', age=7, notes='not the nicest...', available=False)

    mojo = Pet(name='Mojo', species='Cat', photo_url='https://i.pinimg.com/564x/bd/3d/e3/bd3de3cd353afdbac5388426c885fabf.jpg', age=5, notes='likes laying in the sun. unfortunately is not suitable to go outside unattended', available=False)

    db.session.add(milo)
    db.session.add(marvin)
    db.session.add(mojo)

    db.session.commit()