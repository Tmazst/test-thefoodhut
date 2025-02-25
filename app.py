# This is a car sale website for Eswatini agents, owners, garages and car sales stores
# They advertise new and second cars of any brand
# They can also sale spare parts when stripping they cars

from flask import Flask,render_template,url_for,redirect,request,flash,session,jsonify
from flask_login import login_user, LoginManager,current_user,logout_user, login_required
from Forms import *
from models import *
from flask_bcrypt import Bcrypt
# import Users_Data
import secrets
import os
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
# from bs4 import BeautifulSoup as bs
# from flask_colorpicker import colorpicker
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
# import pyodbc
import time
import sqlite3
import itsdangerous
import random
import glob
# from twilio.rest import Client


#Change App
app = Flask(__name__)
app.config['SECRET_KEY'] = "sdkh77sdjfe832j2rj_32j"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///vakasha_explorer2_db.db"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle':280}
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOADED"] = 'static/uploads'

ser = Serializer(app.config['SECRET_KEY']) 

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Log in
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

application=app

ALLOWED_EXTENSIONS = {"txt", "xlxs",'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Function to check if the file has an allowed extension
def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class user_class:
    s = None

    def get_reset_token(self, c_user_id):

        s = Serializer(app.config['SECRET_KEY'])

        return s.dumps({'user_id': c_user_id, 'expiration_time': time.time() + 300}).encode('utf-8')

    @staticmethod
    def verify_reset_token(token, expires=1800):

        s = Serializer(app.config['SECRET_KEY'], )

        try:
            user_id = s.loads(token, max_age=300)['user_id']
        except itsdangerous.SignatureExpired:
            flash('Token has expired', 'error')
        except itsdangerous.BadSignature:
            flash('Token is Invalid', 'error')
        except:
            return f'Something Went Wrong'  # f'Token {user_id} not accessed here is the outcome user'

        return user_id


# Function to delete an image from the database
def delete_image(image_name):
    # Check img_1
    result = delete_image_from_column('img_1', image_name)
    if result:
        return f"Image {image_name} deleted."

    # Check img_2
    result = delete_image_from_column('img_2', image_name)
    if result:
        return f"Image {image_name} deleted."

    # Check img_3
    result = delete_image_from_column('img_3', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_4
    result = delete_image_from_column('img_4', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_5
    result = delete_image_from_column('img_5', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_6
    result = delete_image_from_column('img_6', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_7
    result = delete_image_from_column('img_7', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_8
    result = delete_image_from_column('img_8', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_9
    result = delete_image_from_column('img_9', image_name)
    if result:
        return f"Image {image_name} deleted."
    
    # Check img_10
    result = delete_image_from_column('img_10', image_name)
    if result:
        return f"Image {image_name} deleted."

    return f"Image {image_name} not found."

# Function to delete an image from a specific column
def delete_image_from_column(column_name, image_name):
    image = Car_Ads_Images.query.filter(getattr(Car_Ads_Images, column_name) == image_name).first()
    if image:
        file_path = os.path.join(app.root_path, 'static/images', image_name)
        if os.path.exists(file_path):
            os.remove(file_path)

        setattr(image, column_name, None)  # Or set it to an empty string depending on your requirements
        db.session.commit()
        return True
    else:
        return False

def remove_path(image,file_dir):
    pass
    # file_path=None
    # print("Path is: ",os.path.exists(image))
    # if os.path.exists(image):
    #     file_path = os.path.join(app.root_path, file_dir, image)
    # if os.path.exists(file_path):
    #     try:
    #         os.remove(file_path) 
    #     except:
    #         return 'No Such File!'

    # return True

def delete_img(image,token_):
    # Get image row
    image_column = Menus_Images.query.filter_by(token=token_).first()
    if image_column and image_column.img_1 == image:
        try:
            remove_path(image, "static/uploads")
        except:
            return 'No Such File!'

    elif image_column and image_column.img_2 == image:
        try:
            remove_path(image, "static/uploads")
        except:
            return 'No Such File!'
    
    return True


def del_menu_img(image,token_):
    # Get image row
    image_column = Menus_Images.query.filter_by(token=token_).first()

    if image_column and image_column.img_1 == image:
        file_path = os.path.join(app.root_path, 'static/uploads', image)
        remove_path(file_path)
    
    return True


class Dont_Update:
    img = ''
    cur_file = ''

def profile_img(file):
        global img_checker
        img_checker = Dont_Update
        # Avoid duplication of same image in a session 
        if img_checker.img  == file.filename:
            print("File updated")
            return img_checker.cur_file
        else:
        
            filename = secure_filename(file.filename)

            img_checker.img = file.filename

            _img_name, _ext = os.path.splitext(file.filename)
            gen_random = secrets.token_hex(8)
            new_file_name = gen_random + _ext

            print("DEBIG IMAGE: ",new_file_name)

            if file.filename == '':
                return 'No selected file'

            if file.filename:
                file_saved = file.save(os.path.join(app.root_path, 'static/images', new_file_name))
                img_checker.cur_file = new_file_name
                print("File Upload Successful!!")
                return new_file_name

            else:
                return f"Allowed are [ .png, .jpg, .jpeg, .gif] only"


def process_file(file):
        global img_checker
        img_checker = Dont_Update
        # Avoid duplication of same image in a session 
        if img_checker.img  == file.filename:
            print("File updated")
            return img_checker.cur_file
        else:
        
            filename = secure_filename(file.filename)

            img_checker.img = file.filename

            _img_name, _ext = os.path.splitext(file.filename)
            gen_random = secrets.token_hex(8)
            new_file_name = gen_random + _ext

            print("DEBIG IMAGE: ",new_file_name)

            if file.filename == '':
                return 'No selected file'

            if file.filename:
                file_saved = file.save(os.path.join(app.root_path, 'static/uploads', new_file_name))
                img_checker.cur_file = new_file_name
                return new_file_name

            else:
                return f"Allowed are [ .png, .jpg, .jpeg, .gif] only"


def menu_pictures(images_uploads):

    uploaded_files = images_uploads
    img_names_ls = []
    img_string = ''

    if uploaded_files:
        for file in uploaded_files:
            print("Image: ",file.filename)
            filename = secure_filename(file.filename)
            print("Filename: ",filename)
            _img_name, _ext = os.path.splitext(file.filename)
            gen_random = secrets.token_hex(8)
            new_file_name = gen_random + _ext

            # Append image to img_names
            img_names_ls.append(new_file_name)

            # Save image in the server 
            if file:
                file.save(os.path.join(app.config['UPLOADED'], new_file_name))
                print("File Saved : ",file.filename)

    for image in img_names_ls:
        img_string += '_'+image
        print("Check Images: ",img_string)
    print("Check Images: ",uploaded_files)

    return img_names_ls

encry_pw = Bcrypt()


def randomize():

    # Define the range and the number of random numbers you want
    min_value = 3
    max_value = 10
    count = 8  # Number of random numbers to generate

    # Generate a list of random numbers
    random_numbers = [random.randint(min_value, max_value) for _ in range(count)]

    return random_numbers


arg = "tel:761256156"

# Function to retrieve all image files from a directory
def get_all_images_from_directory(directory_path, extensions=("*.jpg", "*.png", "*.jpeg")):
    """
    Retrieve all image files from the specified directory.

    Args:
        directory_path (str): Path to the directory containing images.
        extensions (tuple): List of file extensions to look for (default: jpg, png, jpeg).

    Returns:
        list: List of file paths for images in the directory.
    """
    image_files = []
    
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(directory_path, ext)))
    
    return image_files


@app.context_processor
def inject_ser():
    ser = Serializer(app.config['SECRET_KEY'])  # Define or retrieve the value for 'ser'
    date_today = datetime.now().strftime("%d %b %y - %H:%M")

    directory_path = "static/images/glob_images"
    slider_images = get_all_images_from_directory(directory_path)
    print("Images: ",slider_images)
    

    return dict(ser=ser,date_today=date_today,random_3_10 = randomize(),slider_images=slider_images,Slider=False)

class Contacts:
    contact = None




@app.route('/', methods=["POST","GET"])
def home():

    menu_banner = "Menu Banner"
    layout = None

    comp_ids = {companies.cid for companies in Menu_Items.query.all()}

    # flash(f"This Runs twice","warning")
    query_menu = Menu_Items.query.filter_by(cid=1).all()
    food_groups = {group.item_food_group for group in query_menu}
    for item in food_groups:
        print("Item: ", item)
    
    if request.method=='GET' and request.args.get('icon'):
        layout=request.args.get('icon')
    for comp_id in comp_ids:
        print("COMP ID: ",comp_id)

    return render_template("index.html", comp_ids=comp_ids, companies=entertainer_user, usr=User,menu_banner = menu_banner,layout=layout,Slider=True,
                           query_menu=query_menu,food_groups=food_groups,menu_images=Menus_Images)

class store_cid:
    stored_cid = None
    stored_fitem = None

@app.before_request
def set_flag():
    if 'route_executed' not in request.environ:
        request.environ['route_executed'] = False
        
from check_route import Check_Route as cr


@app.route('/menu', methods=["POST","GET"])
def menu():

    # flash(f"This Runs twice","warning")
    query_menu = Menu_Items.query.filter_by(cid=1).all()
    food_groups = {group.item_food_group for group in query_menu}
    for item in food_groups:
        print("Item: ", item)


    return render_template("menu.html",query_menu=query_menu,food_groups=food_groups,menu_images=Menus_Images)


@app.route("/posts", methods=['POST','GET'])
def posts():

    page_info = "Get a Quick Reply with your best meal, accomodation, chill Eswatini at Your Best Interests and Budget!"
    # page_info = "VnE Helps you find Best Meals at your budget"
    # page_info = "We help you discover how amazing Eswatini is, unbelievable scenarios for having fun"
    # page_info = "You can a amazing meals, and best outing experince at any budget, we are here to help you"
    # page_info = "Meet your entertainers and get what you want customized just for you"

    title = "Vakasha 'n Explore"
    comments_form =PostCommentForm()
    likes_form =PostCommentForm()
    vac_posts = vacationers_posts.query.order_by(vacationers_posts.timestamp.desc()).all()
    contact = None

    def count_reactions():
        from sqlalchemy import text

        users = []
        all = text(f"SELECT COUNT(*) as total_jobs FROM car_details where user_id={current_user.id}")
        jobs = db.session.execute(all).scalar()

        return jobs


    if request.method == 'POST':
        post_id_ = request.args.get("postid")
        if comments_form.post_id.data:
            post_comment = post_comments(
                post_id=int(ser.loads(comments_form.post_id.data)['data']),comment=comments_form.comment.data,comment_by=current_user.id,
                timestamp=datetime.now(timezone.utc)
            )
            db.session.add(post_comment)
            db.session.commit()


    elif request.method == 'GET':
        print("Check Like: ",likes_form.post_id.data)
        if current_user.is_authenticated:
            if request.args.get('post_id'):
                postid = ser.loads(request.args.get('post_id'))['data']
                post_like = post_likes(
                    post_id=int(postid),usr_id=current_user.id,
                    timestamp=datetime.now()
                )
                validate_like = post_likes.query.filter_by(post_id=postid,usr_id=current_user.id).first()
                
                if not validate_like:
                    db.session.add(post_like) 
                    db.session.commit()


    return render_template("posts.html",vac_posts=vac_posts,page_info=page_info,usr=User,contact=contact,comments_form=comments_form,postlikes=post_likes)


@app.route("/vac_signup", methods=["POST","GET"])
def sign_up():

    register = UserForm()
    user = None

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':

        if register.validate_on_submit():    

            hashd_pwd = encry_pw.generate_password_hash(register.password.data).decode('utf-8')

            if register.company_signup.data:
                user = entertainer_user(name=register.name.data, email=register.email.data, password=hashd_pwd,
                        confirm_password=hashd_pwd,image="default.jpg",company_contacts=register.contacts.data,role = 'company_user',
                        timestamp=datetime.now(timezone.utc))
            else:
                user = vacationer_user(name=register.name.data, email=register.email.data, password=hashd_pwd,
                        confirm_password=hashd_pwd,image="default.jpg",contacts=register.contacts.data,
                        timestamp=datetime.now(timezone.utc),role = 'vacationer_user')
                             
            print('Role Checked!: ',user.role)

            # try:
            if not UserForm().validate_email(register.email.data):
                db.session.add(user)
                db.session.commit()
                print('Sign up successful!')
                flash(f"Account Successfully Created for {register.name.data}", "success")
            else:
                flash(f"Something went wrong, check for errors", "error")
                print('Sign up unsuccessful')
            return redirect(url_for('login'))
            # except: # IntegrityError:
            #     pass

        elif register.errors:
            flash(f"Account Creation Unsuccessful ", "error")
            print(register.errors)

    # from myproject.models import user
    return render_template("vac-signup-form.html",register=register)
 


@app.route("/vac_account", methods=["POST","GET"])
@login_required
def vac_account():

    update_acc = VacationerUserForm()

    vac_user = vacationer_user.query.get(current_user.id)

    print("DEBUG AGENT: ",vac_user.name)

    image_fl = url_for('static', filename='images/image.jpg')

    if request.method == 'POST':

        if update_acc.validate_on_submit():    
            
            # hashd_pwd = encry_pw.generate_password_hash(update_acc.password.data).decode('utf-8')
            vac_user.name = update_acc.name.data
            # print("IMAGE: ",update_acc.image_pfl.data,request.args.get("image_pfl"))
            if update_acc.image.data:
                img_new = profile_img(update_acc.image.data)
                if img_checker:
                    vac_user.image = img_new

            vac_user.contacts = update_acc.contacts.data
            vac_user.whatsapp = update_acc.whatsapp.data
            vac_user.facebook = update_acc.facebook.data
            vac_user.date_of_birth = update_acc.date_of_birth.data
            vac_user.personal_id_no = update_acc.personal_id_no.data
            vac_user.zip_code = update_acc.zip_code.data
            vac_user.address = update_acc.address.data

            db.session.commit()
            print("DOES IT VALIDATE")

        elif update_acc.errors:
            flash(f"Update Unsuccessful ", "error")
            print(update_acc.errors)

    # from myproject.models import user
    return render_template("user_acc.html",update_acc=update_acc,vac_user=vac_user)


@app.route("/entertainer_signup", methods=["POST","GET"])
def entertainer_sign_up():

    register = EntertainerUserForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':

        if register.validate_on_submit():    

            hashd_pwd = encry_pw.generate_password_hash(register.password.data).decode('utf-8')
            entertain_user = entertainer_user(name=register.name.data, email=register.email.data, password=hashd_pwd,
                        confirm_password=hashd_pwd,image="logo_template.png",company_profile_img="picture_template.png",contacts=register.contacts.data,company_address=register.company_address.data,
                        industry_category=register.industry_category.data,web_link=register.web_link.data,facebook=register.facebook.data,
                        twitter_link=register.twitter_link.data,youtube_link=register.youtube_link.data,payment_options=register.payment_options.data,
                        timestamp=datetime.now(timezone.utc),role='company_user') 

            try:
                if not UserForm().validate_email(register.email.data):
                    db.session.add(entertain_user)
                    db.session.commit()
                    flash(f"Account Successfully Created for {register.name.data}", "success")
                else:
                    flash(f"Something went wrong, check for errors", "error")
                return redirect(url_for('login'))
            except: # IntegrityError:
                pass

        elif register.errors:
            flash(f"Account Creation Unsuccessful ", "error")
            print(register.errors)

    # from myproject.models import user
    return render_template("entertainer-sign-up.html",register=register)


@app.route("/entertainment_account", methods=["POST","GET"])
@login_required
def entertainment_account():

    entertain_user = entertainer_user.query.get(current_user.id)
    update_acc = EntertainerUserForm(obj=entertain_user)

    print("DEBUG AGENT: ",entertain_user.name)

    image_fl = url_for('static', filename='images/image.jpg')

    if request.method == 'POST':

        if update_acc.validate_on_submit():    
            
            # hashd_pwd = encry_pw.generate_password_hash(update_acc.password.data).decode('utf-8')
            entertain_user.name = update_acc.company_name.data
            # print("IMAGE: ",update_acc.image.data,request.args.get("image"))
            if update_acc.logo.data and not update_acc.logo.data == entertain_user.image:
                img_new = profile_img(update_acc.logo.data)
                if img_checker:
                    entertain_user.image = img_new

            if update_acc.company_profile_img.data and not update_acc.company_profile_img.data == entertain_user.company_profile_img:
                img_new = profile_img(update_acc.company_profile_img.data)
                if img_checker:
                    entertain_user.company_profile_img = img_new

            entertain_user.whatsapp = update_acc.whatsapp.data
            entertain_user.zip_code = update_acc.zip_code.data
            entertain_user.company_address = update_acc.company_address.data
            entertain_user.company_contacts = update_acc.company_contacts.data
            entertain_user.industry_category = update_acc.industry_category.data
            entertain_user.web_link = update_acc.web_link.data
            entertain_user.facebook = update_acc.facebook.data
            entertain_user.twitter_link = update_acc.twitter_link.data
            entertain_user.youtube_link = update_acc.youtube_link.data
            entertain_user.region = update_acc.region.data
            entertain_user.coordinates = update_acc.coordinates.data
            entertain_user.payment_options = update_acc.payment_options.data


            db.session.commit()
            flash(f"Update Successful!", "success")

        elif update_acc.errors:
            flash(f"Update Unsuccessful ", "error")
            print(update_acc.errors)

    # from myproject.models import user
    return render_template("entertainment_acc.html",update_acc=update_acc,entertain_user=entertain_user)


@app.route("/login", methods=["POST","GET"])
def login():

    login = Login()

    print(f"Submtion: ")
    if request.method == 'POST':
        print(f"Submtion: ")

        if login.validate_on_submit():    

                user_login = User.query.filter_by(email=login.email.data).first()
                print(f"Query: ",user_login)
                # flash(f"Hey! {user_login.password} Welcome", "success")
                if user_login and encry_pw.check_password_hash(user_login.password, login.password.data):
                    login_user(user_login)
                    # print("Creditantials are ok")
                    print("No Verification Needed: ", user_login.verified)
                    req_page = request.args.get('next')
                    flash(f"Hey! {user_login.name.title()} You're Logged In!", "success")
                    return redirect(req_page) if req_page else redirect(url_for('home'))
                    # if user_login:
                    # # if not user_login.verified:
                    #     return redirect(url_for('verification'))
                    # else:
                    #     # After login required prompt, take me to the page I requested earlier
                    #     print("No Verification Needed: ", user_login.verified)
                    #     req_page = request.args.get('next')
                    #     flash(f"Hey! {user_login.name.title()} You're Logged In!", "success")
                    #     return redirect(req_page) if req_page else redirect(url_for('home'))
                else:
                    flash(f"Login Unsuccessful, please use correct email or password", "error")

        else:
            print("No Validation")
            if login.errors:
                for error in login.errors:
                    print("Errors: ", error)
            else:
                print("No Errors found", login.email.data, login.password.data)

    return render_template("login.html",login=login)


@app.route("/forgot_password", methods=['POST', "GET"])
def reset_request():
    reset_request_form = Reset_Request()

    if current_user.is_authenticated:
        logout_user()

    if request.method == 'POST':
        if reset_request_form.validate_on_submit():
            # Get user details through their email
            usr_email = User.query.filter_by(email=reset_request_form.email.data).first()

            if usr_email is None:
                # print("The email you are request for is not register with T.H.T, please register first, Please Retry")
                flash(
                    "The email you are requesting a password reset for, is not registered with VnE, please register as account first",
                    'error')

                return redirect(url_for("reset_request"))

            def send_link(usr_email):
                app.config["MAIL_SERVER"] = "smtp.googlemail.com"
                app.config["MAIL_PORT"] = 587
                app.config["MAIL_USE_TLS"] = True
                em = app.config["MAIL_USERNAME"] = os.getenv("EMAIL")
                app.config["MAIL_PASSWORD"] = "abng vekb agyv osbw" #os.getenv("PWD")

                mail = Mail(app)

                token = user_class().get_reset_token(usr_email.id)
                msg = Message("Password Reset Request", sender="noreply@demo.com", recipients=[usr_email.email])
                msg.body = f"""Good day, {usr_email.name}
                
You have requested a password reset for your The Vakasha n Explore Account.
To reset your password, visit the following link:{url_for('reset_request', token=token, _external=True)}

If you did not requested the above message please ignore it, and your password will remain unchanged.
"""

                try:
                    mail.send(msg)
                    flash('An email has been sent with instructions to reset your password', 'success')
                    return "Email Sent"
                except Exception as e:

                    flash('Ooops, Something went wrong Please Retry!!', 'error')
                    return "The mail was not sent"

            # Send the pwd reset request to the above email
            send_link(usr_email)

            return redirect(url_for('login'))

    return render_template("forgot_password.html", reset_request_form=reset_request_form)



@app.route("/verification", methods=["POST", "GET"])
# User email verification @login
# @login the user will register & when the log in the code checks if the user is verified first...
def verification():

    usr_ = User.query.get(current_user.id)

    def send_veri_mail():

        app.config["MAIL_SERVER"] = "smtp.googlemail.com"
        app.config["MAIL_PORT"] = 587
        app.config["MAIL_USE_TLS"] = True
        # Creditentials saved in environmental variables
        em = app.config["MAIL_USERNAME"] = "pro.dignitron@gmail.com"  # os.getenv("MAIL")
        app.config["MAIL_PASSWORD"] = os.getenv("PWD")
        app.config["MAIL_DEFAULT_SENDER"] = 'VnE <no-reply@gmail.com>'
        app.config["MAIL_DEFAULT_SENDER"] = "noreply@gmail.com"

        mail = Mail(app)

        token = user_class().get_reset_token(current_user.id)
        usr_email = usr_.email

        msg = Message(subject="Email Verification", sender="no-reply@gmail.com", recipients=[usr_email])

        msg.body = f"""Hi, {usr_.name}
            
Please follow the link below to verify your email with The Hustlers Time:
            
Verification link;
{url_for('verified', token=token, _external=True)}
        """
        try:
            mail.send(msg)
            flash(f'An email has been sent with a verification link to your email account', 'success')
            return "Email Sent"
        except Exception as e:
            flash(f'Email not sent here', 'error')
            return "The mail was not sent"

    try:
        if not usr_.verified:
            send_veri_mail()
        else:
            return redirect(url_for("home"))
    except:
        flash(f'Debug {usr_.email}', 'error')
        return redirect(url_for("login"))

    return render_template('verification.html')


@app.route("/verified/<token>", methods=["POST", "GET"])
# Email verification link verified with a token
def verified(token):
    # Check to verify the token received from the user email
    # process the user_id for the following script
    user_id = user_class.verify_reset_token(token)

    try:
        usr = User.query.get(user_id)
        usr.verified = True
        db.session.commit()
        if usr.verified:
            qry_usr = User.query.get(user_id)
            if not current_user.is_authenticated:
                login_user(usr)
            flash(f"Welcome, {qry_usr.name}; Please Finish Updating your Profile!!", "success")
            # return redirect(url_for('account'))
    except Exception as e:
        flash(f"Something went wrong, Please try again ", "error")

    return render_template('verified.html')


# Flask route to search for a value in all columns of a table
@app.route('/search', methods=['GET'])
def search_in_table():

    specials_qry = Specials_n_Offers

    search_value = request.args.get('search_value')
    table_name = "car_details" #request.args.get('table_name')

    # Get the root directory of the Flask application
    root_dir = os.path.abspath(os.path.dirname(__file__))

    # Construct the path to the SQLite database file inside the instance folder
    db_file_path = os.path.join(root_dir, 'instance', 'vakasha_explore_db.db')

    # conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    query = f"SELECT * FROM {table_name} WHERE (COALESCE(car_make, '') || COALESCE(car_model, '') || COALESCE(vehicle_id_number, '') || COALESCE(year, '')) LIKE ?"
    cursor.execute(query, ('%' + search_value + '%',))
    rows = cursor.fetchall()

    for row in rows:
        print("Specail: ",row)

    # Convert the results to a list of dictionaries
    results = [{'Column1': row[0], 'Column2': row[1]} for row in rows]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return render_template('search_results.html',rows=rows,images_qry='')

# <a class="view_user" href="/user_viewed?id={{ser.dumps({'data6':item.id})}}">View</a>

@app.route('/enquiry_posts', methods=["POST","GET"])
@login_required
def enquiry_posts():

    enquiry_posts_ = VacationersPostForm()
    
    if request.method == "POST":

        # print("Check Images Before: ",request.files.getlist("car_images"))
        if enquiry_posts_.validate_on_submit():

            enquiry_post = vacationers_posts(
                user_id = current_user.id, looking_for=enquiry_posts_.looking_for.data,no_of_people=enquiry_posts_.no_of_people.data,
                specify_food=enquiry_posts_.specify_food.data,specify_drinks=enquiry_posts_.specify_drinks.data,#prefered_date=enquiry_posts_.prefered_date.data,
                food_drinks_budget=enquiry_posts_.food_drinks_budget.data,places_of_interest=enquiry_posts_.places_of_interest.data,facilities=enquiry_posts_.facilities.data,
                other_places_options=enquiry_posts_.other_places_options.data,accomodation_budget=enquiry_posts_.accomodation_budget.data,
                timestamp = datetime.now()
            )

            db.session.add(enquiry_post)
            db.session.commit() 

            print("Uploaded Successfully!")
            flash("Uploaded Successfully!","success")
        else:
            if enquiry_posts_.errors:
                for error in enquiry_posts_.errors:
                    print("Errors: ", error)

    return render_template("enquiry-post-form.html",enquiry_posts_=enquiry_posts_)


@app.route('/post_comments_form', methods=["POST","GET"])
@login_required
def post_comments_form():
    pass


@app.route('/special_offers_form', methods=["POST","GET"])
@login_required
def special_offers_form():

    special_offers_ = SpecialsOffersForm()

    if request.method == "POST":

        if special_offers_.validate_on_submit():

            special_offer = Specials_n_Offers(
                ent_user_id = current_user.id, #poster_ad=special_offers_.poster_ad.data,
                additional_comments=special_offers_.additional_comments.data,timestamp=datetime.now(timezone.utc), 
                special_call=special_offers_.special_call.data,contact_person=special_offers_.contact_person.data
            )

            if special_offers_.poster_ad.data:
                # print("Special Offers: ",special_offers_.poster_ad.data.filename)
                img_new = process_file(special_offers_.poster_ad.data)
                
                if img_new:
                    special_offer.poster_ad = img_new

            db.session.add(special_offer)
            db.session.commit() 

            flash("Uploaded Successfully!","success")
        else:
            if  special_offers_.errors:
                for error in  special_offers_.errors:
                    print("Errors: ", error)

    return render_template("special-offer-form.html", special_offers_= special_offers_)


@app.route('/special_offers', methods=["POST","GET"])
def special_offers():
    page_info = " "
    offers_query = Specials_n_Offers.query.all()

    return render_template("special_offers_ads.html", offers_query= offers_query,usr=User,page_info=page_info,Slider=True)


@app.route('/manage_special_offers', methods=["POST","GET"])
@login_required
def manage_special_offers():

    offers_query = Specials_n_Offers.query.get(ent_user_id=current_user.id)

    def count_ads():
        from sqlalchemy import text

        users = []
        all = text(f"SELECT COUNT(*) as total_jobs FROM car_details where user_id={current_user.id}")
        jobs = db.session.execute(all).scalar()

        return jobs

    return render_template("/manage_special_offers.html", offers_query=offers_query,no_of_ads=count_ads())


@app.route('/edit_special_offer', methods=["POST","GET"])
@login_required
def edit_special_offer():

    special_offers_ = SpecialsOffersForm()

    if request.args.get("oid"):
        oid_ = ser.loads(request.args.get("oid"))['data']
        offer_query = Specials_n_Offers.query.get(oid_)

        form = request.form

        if special_offers_.validate_on_submit():

            offer_query.poster_ad=special_offers_.poster_ad.data
            offer_query.additional_comments=form['additional_comments']
            offer_query.special_call=form['special_call']
            offer_query.contact_person=form['contact_person']

            if form['poster_ad']:
                img_new = process_file(form['poster_ad'])
                if img_checker:
                    offer_query.image = img_new

            db.session.commit() 
            flash("Update Successful!","success")

        else:
            if  special_offers_.errors:
                for error in  special_offers_.errors:
                    print("Errors: ", error)

    return render_template("/manage_special_offers.html", special_offers_= special_offers_,offer_query=offer_query)


@app.route('/menu_item_form', methods=["POST","GET"])
@login_required
def menu_form():

    menu_item_form = MenuItemForm()

    no_of_menu_itms=len(Menu_Items.query.filter_by(cid=current_user.id).all())

    if menu_item_form.validate_on_submit():

        menu_item = Menu_Items(
            item_name = menu_item_form.item_name.data,item_caption = menu_item_form.item_caption.data,
            item_description = menu_item_form.item_description.data,item_ingredients = menu_item_form.item_ingredients.data,
            item_food_group = menu_item_form.item_food_group.data,item_price = menu_item_form.item_price.data,
            token = str(datetime.timestamp(datetime.now())),cid=current_user.id
            )
 
        db.session.add(menu_item)

        if menu_item_form.main_img.data:
            menu_item.main_img=process_file(menu_item_form.main_img.data)
            # process_file(menu_item_form.main_img.data)
        db.session.commit() 

        # Query the current Item 
        query_curr_item =  Menu_Items.query.filter_by(token=menu_item.token).first()

        pictures = Menus_Images(menu_item_id=query_curr_item.id, token=menu_item.token)

        db.session.add(pictures)

        for i, img_str in enumerate(menu_pictures(request.files.getlist("images"))):
            if i == 0:
                pictures.img_1 = img_str
            elif i == 1:
                pictures.img_2 = img_str

        db.session.commit() 
        flash("Activity was Successful!","success")

    else:
        if  menu_item_form.errors:
            for error in  menu_item_form.errors:
                print("Errors: ", error)

    return render_template("menu_item_form.html", menu_item_form=menu_item_form, no_of_menu_itms=no_of_menu_itms)


@app.route('/orders', methods=["POST","GET"])
@login_required
def orders():

    orders = None
    if current_user.role == 'company_user':
        orders= Menu_Orders.query.filter_by(cid=current_user.id).all()
    
    return render_template('orders.html', orders=orders, usr=User,menu_item=Menu_Items)


@app.route('/menu_item_edit', methods=["POST","GET"])
@login_required
def menu_form_edit():

    no_of_menu_itms=len(Menu_Items.query.filter_by(cid=current_user.id).all())
    menu_item = Menu_Items.query.filter_by(cid=current_user.id,id=ser.loads(request.args.get("mid"))['data']).first()
    item_edit_form = MenuItemForm(obj=menu_item)
    images = Menus_Images.query.filter_by(token = menu_item.token).first()

    if request.method == "POST":
        print("Check Description: ",request.form.get("item_description"))
        menu_item.item_name = item_edit_form.item_name.data
        menu_item.item_caption = item_edit_form.item_caption.data
        menu_item.item_description = request.form.get("item_description")
        menu_item.item_ingredients = item_edit_form.item_ingredients.data
        menu_item.item_food_group = item_edit_form.item_food_group.data
        menu_item.item_price = item_edit_form.item_price.data

        # images = Menus_Images.query.filter_by(token = menu_item.token).first()
        if item_edit_form.main_img.data and not item_edit_form.main_img.data == menu_item.main_img:
            remove_path(menu_item.main_img,"static/uploads")
            menu_item.main_img=process_file(item_edit_form.main_img.data)

        if len(request.files.getlist("images")) > 1:
            print("IMAGES DEBUG: ", len(request.files.getlist("images")))
            if images.img_1:
                delete_img(images.img_1,images.token)
            if images.img_2:
                delete_img(images.img_2,images.token)
            for i, img_str in enumerate(menu_pictures(request.files.getlist("images"))):
                if i == 0:
                    images.img_1 = img_str
                elif i == 1:
                    images.img_2 = img_str

        db.session.commit()
        flash("Update Successful","success")

    return render_template("item_edit_form.html", item_edit_form=item_edit_form,no_of_menu_itms=no_of_menu_itms,menu_item=menu_item,images=images)


@app.route('/places', methods=["POST","GET"])
def places():
    
    companies = companies.query.all()

    return render_template("places.html", companies=companies, companys=entertainer_user,usr=User,menu_banner = menu_banner)



@app.route('/place_order', methods=["POST","GET"])
@login_required
def place_order():

    item = Menu_Items.query.get(ser.loads(request.args.get("mid"))['data'])

    #Email Company
    
    order_qty=1

    if request.method == 'POST':
       form = request.form
       orders = Menu_Orders(menu_item_id = form['mid'],
       cid = item.cid,
       vacid = current_user.id,
       order_qty = form['qty'],
       timestamp = datetime.now()
       )

    #    db.session.add(orders)
    #    db.session.commit()

       return f'Thank You, This page is Under Construction'

    return render_template("place_order.html", item=item, order_qty=order_qty)


# Menu Filter =================================
# @app.route('/menu--', methods=['GET', 'POST'])
# def menu_():
#     cid_ = ...  # Get the customer ID based on your logic
#     query_menu = Menu_Items.query.filter_by(cid=cid_).all()
    
#     # Fetch unique food groups
#     food_groups = {item.food_group for item in query_menu}
    
#     selected_group = request.args.get('food_group')  # Get the selected food group from query parameters
    
#     # Filter menu items by selected food group
#     if selected_group:
#         filtered_menu_items = [item for item in query_menu if item.food_group == selected_group]
#     else:
#         filtered_menu_items = query_menu  # Show all if no filter is applied
    
#     return render_template('menu.html', 
#                            menu_items=filtered_menu_items, 
#                            food_groups=sorted(food_groups),
#                            selected_group=selected_group)
# ===========================================================


@app.route('/delete_entry')
def delete_entry():
    if request.method == "GET":
        if request.args.get("del"):
            uidel = request.args.get("del")
            id_ = ser.loads(uidel)['data']

            #Check if the user is not currently hired somewhere
            item_to_del = vacationers_posts.query.get(id_)
            if item_to_del:
                db.session.delete(item_to_del)
                db.session.commit()
                print(f"File Deleted: {item_to_del}")
                return redirect(url_for("ads_perfomances"))
            
    return  f"File Deleted"      


@app.route('/delete_comment')
def delete_comment():
    if request.method == "GET":
        if request.args.get("del"):
            uidel = request.args.get("del")
            id_ = ser.loads(uidel)['data']

            #Check if the user is not currently hired somewhere
            item_to_del = post_comments.query.get(id_)
            if item_to_del:
                db.session.delete(item_to_del)
                db.session.commit()
                print(f"File Deleted: {item_to_del}")
                return redirect(url_for("home"))
            
    return  f"File Deleted"          


@app.route('/logout')
def log_out():

    logout_user()

    return redirect(url_for('home'))


@app.route("/contact", methods=["POST", "GET"])
def contact_us(user_sentto_mail=None):

    contact_form = Contact_Form()
    if request.method == "POST":
        if contact_form.validate_on_submit():
            def send_link():
                app.config["MAIL_SERVER"] = "smtp.googlemail.com"
                app.config["MAIL_PORT"] = 587
                app.config["MAIL_USE_TLS"] = True
                em = app.config["MAIL_USERNAME"] = os.environ.get("EMAIL")
                if not user_sentto_mail:
                    user_sentto_mail = em
                app.config["MAIL_PASSWORD"] = os.environ.get("PWD")

                mail = Mail(app)

                msg = Message(contact_form.subject.data, sender=em, recipients=[user_sentto_mail])
                msg.body = f"""{contact_form.message.data}\n
{contact_form.email.data}
                    """

                try:
                    mail.send(msg)
                    flash("Your Message has been Successfully Sent!!", "success")
                    return "Email Sent"
                except Exception as e:
                    # print(e)
                    flash(f'Ooops Something went wrong!! Please Retry', 'error')
                    return "The mail was not sent"

                # Send the pwd reset request to the above email
            send_link()

            #print("Posted")
        else:
            flash("Ooops!! Please be sure to fill both email & message fields, correctly","error")

    return render_template("contact.html",contact_form=contact_form)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
