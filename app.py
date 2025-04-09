from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from forms import NewPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'NotPassword'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

'''Shows all pets from adopt_db with pet name photo and availability status'''
@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home_page.html', pets=pets)

'''Shows the add pet form and handles the submitted add pet form. Creates a new pet with new pet form data and commits it to db. Checks if there is a provided photo_url, if not, lets default url from pet model take over.'''
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = NewPetForm()

    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet_data = {
            'name': name,
            'species': species,
            'age': age,
            'notes': notes
        }

        if photo_url:
            pet_data['photo_url'] = photo_url

        pet = Pet(**pet_data)

        db.session.add(pet)
        db.session.commit()
        flash('Pet added!')
        return redirect('/')
    
    return render_template('add_pet.html', form=form)


'''Shows specific pet details by getting pet from db with pet_id'''
@app.route('/<int:pet_id>')
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)


'''Shows edit pet form and handles edit pet form. Updates pet and submits it to db.'''
@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if request.method == 'POST' and form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        available = form.available.data
        if available == 'True':
            pet.available = True
        else:
            pet.available = False
        db.session.commit()

        flash('Pet updated!')
        return redirect(f'/{pet_id}')
    return render_template('edit_pet.html', form=form, pet=pet)
