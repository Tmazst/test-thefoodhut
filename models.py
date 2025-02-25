# ----------Actions Required---------#
# 1.Change db.Date() to db.DateTime() in timestamps
# -----------------------------------#


# from alchemy_db import db.Model
from sqlalchemy import  MetaData, ForeignKey
from flask_login import login_user, UserMixin
from sqlalchemy.orm import backref, relationship
from datetime import datetime,timezone
from flask_sqlalchemy import SQLAlchemy
# from app import app

db = SQLAlchemy()


#from app import login_manager

metadata = MetaData()


#Users class, The class table name 'h1t_users_cvs'
class User(db.Model,UserMixin):

    __table_args__ = {'extend_existing': True}

    #Create db.Columns
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    image = db.Column(db.String(30), nullable=True)
    contacts = db.Column(db.String(20))
    whatsapp = db.Column(db.String(50))
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(120), unique=True)
    confirm_password = db.Column(db.String(120), unique=True)
    verified = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    role = db.Column(db.String(120))
    offer_comments_id = relationship("offer_comments", backref='user', lazy=True)
    post_comments_id = relationship("post_comments", backref='user', lazy=True)

    __mapper_args__={
        "polymorphic_identity":'user',
        'polymorphic_on':role
    }


class vacationer_user(User):

    __tablename__ = 'vacationer_user'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    facebook = db.Column(db.String(50))
    personal_id_no = db.Column(db.Integer())
    date_of_birth = db.Column(db.DateTime())
    address = db.Column(db.String(120))
    free_trial = db.Column(db.Boolean())
    zip_code =  db.Column(db.String(120))
    other = db.Column(db.String(120)) #Resume
    vacationers_posts_rel = relationship("vacationers_posts", backref='vacationer_user',lazy=True)

    __mapper_args__={
            "polymorphic_identity":'vacationer_user'
        }


class admin_user(User):

    __tablename__ = 'admin_user'

    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    contacts = db.Column(db.String(20))
    date_of_birth = db.Column(db.DateTime())
    address = db.Column(db.String(120))
    company_name = db.Column(db.String(120))
    department = db.Column(db.String(120))
    position = db.Column(db.String(120)) #Resume
    other = db.Column(db.String(120)) 
    # jobs_applied_for = relationship("Applications", backref='Applications.job_title', lazy=True)
    # hired_user = relationship("hired", backref='Hired Applicant', lazy=True)

    __mapper_args__={
            "polymorphic_identity":'admin_user'
        }


class entertainer_user(User):

    __tablename__ = 'entertainer_user'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    company_address = db.Column(db.String(120))
    company_contacts = db.Column(db.String(120))
    industry_category = db.Column(db.String(120))
    company_profile_img = db.Column(db.String(120))
    web_link = db.Column(db.String(120))
    facebook = db.Column(db.String(120))
    twitter_link = db.Column(db.String(120))
    youtube_link = db.Column(db.String(120))
    region = db.Column(db.String(120)) 
    other = db.Column(db.String(120)) 
    other_0 = db.Column(db.String(120))
    coordinates = db.Column(db.String(120))
    payment_options = db.Column(db.String(100))
    specials_n_offers_rel = relationship("Specials_n_Offers", backref='entertainer_user',lazy=True)
    menu_items = relationship("Menu_Items", backref='entertainer_user',lazy=True)
    # applicantions_posted = relationship("Applications", backref='employer', lazy=True)
    # freelance_job_ads = relationship("Freelance_Jobs_Ads", backref='Freelance_Jobs_Ads.service_title', lazy=True)

    __mapper_args__ = {
        "polymorphic_identity": 'company_user'
    }


class Specials_n_Offers(db.Model,UserMixin):

    __tablename__= "specials_n_offers"

    id = db.Column(db.Integer, primary_key=True)
    ent_user_id = db.Column(db.Integer,ForeignKey('entertainer_user.id'))
    poster_ad = db.Column(db.String(30), nullable=True)
    additional_comments = db.Column(db.String(120))
    timestamp = db.Column(db.Date())
    special_call = db.Column(db.String(120))#Title
    contact_person = db.Column(db.String(120))
    offers_comments_id = relationship("offer_comments", backref='vacationers_posts',lazy=True)


class vacationers_posts(db.Model,UserMixin):

    __tablename__= "vacationers_posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,ForeignKey('vacationer_user.id'))
    looking_for = db.Column(db.String(255))
    specify_food = db.Column(db.String(255))
    specify_drinks = db.Column(db.String(255))
    food_drinks_budget = db.Column(db.String(255))
    places_of_interest = db.Column(db.String(255))
    other_places_options = db.Column(db.String(255))
    accomodation_budget = db.Column(db.String(255))
    facilities = db.Column(db.String(255))
    no_of_people = db.Column(db.String(255))
    prefered_date = db.Column(db.String(255))
    prefered_time = db.Column(db.String(255))
    timestamp = db.Column(db.Date()) #Change to db.DateTime()
    other1 = db.Column(db.String(255))
    other2 = db.Column(db.String(255))
    other3 = db.Column(db.String(255))
    other4 = db.Column(db.String(255))
    other5 = db.Column(db.String(255))
    post_comments_id = relationship("post_comments", backref='vacationers_posts',lazy=True)
    post_likes_id = relationship("post_likes", backref='vacationers_posts',lazy=True)


class post_comments(db.Model,UserMixin):

    __tablename__= "post_comments"

    id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer,ForeignKey('user.id'))
    post_id = db.Column(db.Integer,ForeignKey('vacationers_posts.id'))
    comment = db.Column(db.String(255))
    comment_by = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime()) #Change to db.DateTime()


class post_likes(db.Model,UserMixin):

    __tablename__= "post_likes"

    id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer,ForeignKey('user.id'))
    post_id = db.Column(db.Integer,ForeignKey('vacationers_posts.id'))
    # comment = db.Column(db.String(255))
    comment_by = db.Column(db.Integer)
    timestamp = db.Column(db.Date()) #Change to db.DateTime()



class offer_comments(db.Model,UserMixin):

    __tablename__= "offers_comments"

    id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer,ForeignKey('user.id'))
    ad_id = db.Column(db.Integer,ForeignKey('specials_n_offers.id'))
    comment = db.Column(db.String(255))
    comment_by = db.Column(db.Integer)
    # item_promo_price = db.Column(db.Float(10))
    timestamp = db.Column(db.Date()) #Change to db.DateTime()


# ------------ MENU ------------- #
class Menu_Items(db.Model):

    __tablename__= "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, ForeignKey('entertainer_user.id'))
    item_name = db.Column(db.String(50))
    item_caption = db.Column(db.String(50))
    item_description = db.Column(db.String(255))
    item_ingredients = db.Column(db.String(255))
    item_food_group = db.Column(db.String(50))
    main_img = db.Column(db.String(255))
    item_price = db.Column(db.Float(10))
    item_other = db.Column(db.String(100)) 
    item_other2 = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime())
    token = db.Column(db.String(120), nullable=False)
    menu_item_images = relationship("Menus_Images", backref='menu_items', lazy=True)
    menu_item_order = relationship("Orders", backref='menu_items', lazy=True)


class Menus_Images(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    menu_item_id=db.Column(db.Integer, ForeignKey("menu_items.id"))
    token=db.Column(db.String(120), nullable=False)
    img_1 = db.Column(db.String(120))
    img_2 = db.Column(db.String(120))


class Orders(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    menu_item_id=db.Column(db.Integer, ForeignKey("menu_items.id"))
    vacid=db.Column(db.Integer, ForeignKey('vacationers_posts.id'))
    cid=db.Column(db.Integer, ForeignKey('entertainer_user.id'))
    timestamp=db.Column(db.DateTime())
    # current_location=db.Column(db.String(255))
    # order_qty=db.Column(db.String(255))


class Menu_Orders(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    menu_item_id=db.Column(db.Integer, ForeignKey("menu_items.id"))
    vacid=db.Column(db.Integer, ForeignKey('vacationers_posts.id'))
    cid=db.Column(db.Integer, ForeignKey('entertainer_user.id'))
    timestamp=db.Column(db.DateTime())
    current_location=db.Column(db.String(255))
    order_qty=db.Column(db.Integer())
    other=db.Column(db.Integer())
    other2=db.Column(db.Float())
    other3=db.Column(db.String(255))
    other4=db.Column(db.String(255))

# class VnE_Server_Details(db.Model,UserMixin):

#     __tablename__= "vne_server_details"

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer,ForeignKey('user.id'))
#     car_details = db.Column(db.Integer,ForeignKey('car_details.id'))
#     sale_token = db.Column(db.String(120))
#     car_deal_opened = db.Column(db.String(120))
#     car_deal_closed = db.Column(db.String(120))
#     car_selling_price_agr = db.Column(db.Float(120))
#     other=db.Column(db.String(120))
#     other1=db.Column(db.String(120))
#     other2=db.Column(db.String(120))
#     payment_records = relationship("User_Subscription_Records", backref='vne_server_details', lazy=True)


# class Car_Payment_Records(db.Model,UserMixin):

#     __tablename__= "car_payment_records"

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, ForeignKey('user.id'))
#     car_details_id = db.Column(db.Integer, ForeignKey('car_details.id'))
#     server_details_id = db.Column(db.Integer, ForeignKey('car_server_details.id'))
#     buyer_details = db.Column(db.String(120), ForeignKey('user.id'))
#     sale_token = db.Column(db.String(120))
#     deposit = db.Column(db.Numeric(20))
#     paid_amount = db.Column(db.Float(20))
#     paid_date = db.Column(db.Float(20))
#     paid_balance = db.Column(db.Float(20))
#     other=db.Column(db.String(120))
#     other1=db.Column(db.String(120))
#     other2=db.Column(db.String(120))
 

# class User_Subscription_Records(db.Model,UserMixin):

#     __tablename__= "user_subscription_records"

#     id = db.Column(db.Integer, primary_key=True)
#     # user_id = db.Column(db.Integer, ForeignKey('vne_server_details.id'))
#     subscription_option = db.Column(db.String(120))
#     subscription = db.Column(db.Float(20))
#     subscription_date = db.Column(db.Float(20))
#     paid_balance = db.Column(db.Float(20))
#     other=db.Column(db.String(120))
#     other1=db.Column(db.String(120))
#     other2=db.Column(db.String(120))


# Reference 
class Subscription_Options(db.Model,UserMixin):

    __tablename__= "subscription_options"

    id = db.Column(db.Integer, primary_key=True)
    options_1 = db.Column(db.Float(20))
    options_2 = db.Column(db.Float(20))
    options_3 = db.Column(db.Float(20))
    free_trial = db.Column(db.Float(20))
    other=db.Column(db.String(120))
    other1=db.Column(db.String(120))
    other2=db.Column(db.String(120))







