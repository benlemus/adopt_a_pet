from models import db, Pet
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()
    
    milo = Pet(name='Milo', species='Dog', photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO5U9u20Sw2CyVVLwAjRYjeraJK14UV0EZ5Q&s', age=1,  notes='very very nice and very handsome', available=False)

    marvin = Pet(name='Marvin', species='Cat', photo_url='https://cdn-useast1.kapwing.com/static/templates/woman-yelling-at-cat-meme-template-thumbnail-7c3091cf.webp', age=7, notes='not the nicest...', available=True)

    mojo = Pet(name='Mojo', species='Cat', photo_url='https://i.pinimg.com/564x/bd/3d/e3/bd3de3cd353afdbac5388426c885fabf.jpg', age=5, notes='likes laying in the sun. unfortunately is not suitable to go outside unattended', available=True)

    spikez = Pet(name='Spikez', species='Porcupine', photo_url='https://www.cmzoo.org/wp-content/uploads/prehensile-tailed-porcupine-Mocha-withstrawberry-2023Q-400x600.jpg', age=5, available=True)

    oreo = Pet(name='Oreo', species='Dog', photo_url='https://pbs.twimg.com/media/DuqDAEJV4AAbtZx.jpg:large', age=2, available=True)
    
    gerald = Pet(name='Gerald', species='Porcupine', age=14, available=True)
    
    chester = Pet(name='Chester', species='Cat', photo_url='https://www.usatoday.com/gcdn/presto/2022/10/21/USAT/b3c3545e-d142-441a-89fd-1306e38011be-Rick__A35972049_2022Aug11_0043.jpg?crop=2999,3999,x900,y0', age=8, available=False)

    jack = Pet(name='Jack', species='Dog', photo_url='https://www.orangepet.in/cdn/shop/articles/selective-closeup-cute-kitten-floor_1_600x600_crop_center.jpg?v=1693461218', age=2, available=False)

    db.session.add(milo)
    db.session.add(marvin)
    db.session.add(mojo)
    db.session.add(spikez)
    db.session.add(oreo)
    db.session.add(gerald)
    db.session.add(chester)
    db.session.add(jack)

    db.session.commit()