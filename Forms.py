from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,BooleanField, SelectField,DateField, \
                        URLField,IntegerField,FloatField,MultipleFileField,TelField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from flask_login import current_user
from flask_wtf.file import FileField , FileAllowed
# from wtforms.fields.html5 import DateField,DateTimeField


class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=20)])
    image = StringField('Image')
    contacts = StringField('Contacts', validators=[Length(max=20)])
    whatsapp = StringField('WhatsApp', validators=[Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=120)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=120)])
    company_signup = BooleanField('Sign-up for Company?')
    timestamp = DateField('Timestamp')
    submit = SubmitField('Submit')

    def validate_email(self,email):
        from app import db, User,app

        # with db.init_app(app):
        user_email = User.query.filter_by(email = self.email.data).first()
        if user_email:
            raise ValidationError(f"This email is already registered in this platform")

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Login')
    

class VacationerUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=20)])
    image = FileField('Image (please use passport sized)',)#FileAllowed=['jpg','jpeg','png','svg']
    contacts = StringField('Contacts', validators=[Length(max=20)])
    facebook = StringField('Facebook', validators=[Length(max=50)])
    personal_id_no = StringField('Personal ID Number')
    date_of_birth = DateField('Date of Birth')
    whatsapp = StringField('WhatsApp', validators=[Length(max=50)])
    address = StringField('Address', validators=[Length(max=120)])
    free_trial = BooleanField('Free Trial')
    zip_code = StringField('Zip Code')
    other = StringField('Other', validators=[Length(max=120)])  # Resume
    submit = SubmitField('Submit')


class AdminUserForm(FlaskForm):
    contact = StringField('Contact', validators=[Length(max=20)])
    date_of_birth = DateField('Date of Birth')
    address = StringField('Address', validators=[Length(max=120)])
    company_name = StringField('Company Name', validators=[Length(max=120)])
    department = StringField('Department', validators=[Length(max=120)])
    position = StringField('Position', validators=[Length(max=120)])  # Resume
    other = StringField('Other', validators=[Length(max=120)])
    submit = SubmitField('Submit')


class EntertainerUserForm(FlaskForm):
    company_name = StringField('Company Name', validators=[Length(max=120)])
    company_address = StringField('Company Address', validators=[Length(max=120)])
    company_contacts = StringField('Company Contacts', validators=[Length(max=120)])
    industry_category = StringField('Category', validators=[Length(max=120)])
    zip_code = StringField('Postal Code', validators=[Length(max=20)])
    logo = FileField('Logo',validators=[FileAllowed(['jpg', 'png', 'webp'], 'Images only!')])
    company_profile_img= FileField('Company Profile Image',validators=[FileAllowed(['jpg', 'png', 'webp'], 'Images only!')])
    whatsapp = StringField('WhatsApp', validators=[Length(max=50)])
    web_link = StringField('Web Link', validators=[Length(max=120)])
    facebook = StringField('Facebook Link', validators=[Length(max=120)])
    twitter_link = StringField('Twitter Link', validators=[Length(max=120)])
    youtube_link = StringField('Youtube', validators=[Length(max=120)])
    region = StringField('Region', validators=[Length(max=120)])
    coordinates = StringField('Location Coordinates', validators=[Length(max=120)])
    payment_options = StringField('Payment Options', validators=[Length(max=100)])
    submit = SubmitField('Submit')


class SpecialsOffersForm(FlaskForm):
    poster_ad = FileField('Upload Advert Here:', validators=[FileAllowed(['jpg','png'])])
    additional_comments = TextAreaField('Additional Info', validators=[Length(max=120)])
    timestamp = DateField('Timestamp')
    special_call = StringField('Special Call', validators=[Length(max=120)])
    contact_person = StringField('Contact Person', validators=[Length(max=120)])
    submit = SubmitField('Submit')


class PostCommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Length(max=255)])
    post_id = StringField()
    submit = SubmitField('Submit')


class OfferCommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Length(max=255)])
    post_id = IntegerField()
    submit = SubmitField('Submit')


class VacationersPostForm(FlaskForm):
    looking_for = TextAreaField('Your Enquiry Post ', validators=[Length(max=600)])
    specify_food = StringField('Specify Food & Drinks?', validators=[Length(max=255)])
    specify_drinks = StringField('Specify Drinks', validators=[Length(max=255)])
    food_drinks_budget = StringField('Food Drinks Budget', validators=[Length(max=255)])
    places_of_interest = StringField(' Places of Interest', validators=[Length(max=255)])
    other_places_options = StringField('Other Place Options', validators=[Length(max=255)])
    accomodation_budget = StringField(' Accommodation Budget', validators=[Length(max=255)])
    facilities = TextAreaField(' Facilities', validators=[Length(max=255)])
    no_of_people = StringField('Number of People', validators=[Length(max=255)])
    # prefered_date = DateField('Preferred Date',validators=[])
    # prefered_time = StringField('Preferred Time',validators=[])
    other1 = StringField('Other1', validators=[Length(max=255)])
    other2 = StringField('Other2', validators=[Length(max=255)])
    other3 = StringField('Other3', validators=[Length(max=255)])
    other4 = StringField('Other4', validators=[Length(max=255)])
    other5 = StringField('Other5', validators=[Length(max=255)])
    submit = SubmitField('Submit')


class Reset_Request(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    reset = SubmitField('Submit')

class MenuItemForm(FlaskForm):
    item_name = StringField('Item Name', validators=[Length(max=50)])
    item_caption = StringField('Caption', validators=[Length(max=50)])
    item_description = TextAreaField('Describe', validators=[Length(max=255)])
    item_ingredients = TextAreaField('Ingredients', validators=[Length(max=255)])
    item_price = FloatField('Price')
    item_other = StringField('Food Group', validators=[Length(max=255)])
    item_other2 = StringField('Food Group', validators=[Length(max=255)])
    main_img = FileField('Upload Main Pic:', validators=[FileAllowed(['jpg','png',"jpeg","gif","webp","svg","bmp","tiff","tif","heic"])])
    images = MultipleFileField('Upload Other Pictures - maximum of 2 pictures:', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Submit')
    item_food_group = SelectField('Food Group', choices=[
                                                        ('PIZZA', 'Pizzas'),
                                                        ('DRINK', 'Drinks'),
                                                        ('DESSERT', 'Desserts'),
                                                        ('APPETIZER', 'Appetizers'),
                                                        ('MAIN_COURSE', 'Main Courses'),
                                                        ('SALAD', 'Salads'),
                                                        ('SANDWICH', 'Sandwiches'),
                                                        ('SNACK', 'Snacks'),
                                                        ('SEAFOOD', 'Seafood'),
                                                        ('VEGAN', 'Vegan Dishes'),
                                                        ('VEGETARIAN', 'Vegetarian Dishes'),
                                                        ('PASTA', 'Pasta'),
                                                        ('BURGER', 'Burgers'),
                                                        ('BREAKFAST', 'Breakfast Items'),
                                                        ('SOUP', 'Soups'),
                                                        ('GRILLED', 'Grilled Items'),
                                                        ('SPECIALTY', 'Specialty Dishes'),
                                                        ('SIDE', 'Sides'),
                                                        ('KIDS', 'Kids Menu'),
                                                        ('COCKTAIL', 'Cocktails'),
                                                        ('SMOOTHIE', 'Smoothies'),
                                                        ('COFFEE', 'Coffee & Tea'),
                                                        ('BAKED', 'Baked Goods'),
                                                        ('CHARCUTERIE', 'Charcuterie Boards'),
                                                        ('TRADITIONAL', 'Traditional Dishes'),
                                                        ('GOURMET', 'Gourmet Meals'),
                                                        ('INTERNATIONAL', 'International Cuisine'),
                                                        ('GLUTEN_FREE', 'Gluten-Free Options'),
                                                        ('COMBO', 'Combo Meals'),
                                                        ('SPECIALS', 'Daily Specials'),
                                                        ])