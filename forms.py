from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, FileField
from wtforms.validators import URL, NumberRange, Optional
from flask_wtf.file import FileAllowed

photo_msg = 'Not a valid photo URL.'
age_msg = 'Not a valid age. Must be between 1 and 30.'

class NewPetForm(FlaskForm):
    name = StringField('Name')

    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])

    file = FileField('File Upload', validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg', 'pdf', 'docx'], 'Invalid file type')])
    
    photo_url = StringField('Photo Url', validators=[Optional(), URL(require_tld=True, message=photo_msg)])

    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message=age_msg)])

    notes = TextAreaField('Notes')

class EditPetForm(FlaskForm):
    file = FileField('File Upload', validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg', 'pdf', 'docx'], 'Invalid file type')])

    photo_url = StringField('Photo Url', validators=[Optional(), URL(require_tld=True, message=photo_msg)], default='hello')

    notes = TextAreaField('Notes')

    available = SelectField('Status', choices=[('True', 'Available'), ('False', 'Unavailable')])

    
