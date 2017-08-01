# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, datetime, bcrypt
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        errors = []
        if len(data['first_name'])<2:
            errors.append("First name must consist 2 or more characters.")
        if not data['first_name'].isalpha():
            errors.append("First name must be only letters.")
        if len(data['last_name'])<2:
            errors.append("Last name must consist 2 or more characters.")
        if not data['last_name'].isalpha():
            errors.append("Last name must be only letters.")
        if data['email']=="":
            errors.append("Email address may not be blank.")
        try:
            User.objects.get(email=data['email'])
            Business.objects.get(email=data['email'])
            errors.append("Entered email already exists.")
        except:
            pass
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please enter a valid email address.")
        if len(data['password'])<8:
            errors.append("Password must be at least 8 characters long")
        if data['password']!=data['confirm_password']:
            errors.append("Password and Confirm Password do not match.")

        if len(errors)>0:
            return{
            'new':None,
            'errors_list':errors,
            }
        else:
            data['password']=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            new_user=User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
            return{
            'new':new_user,
            'errors_list':None,
            }

    def login(self, data):
        errors = []
        try:
            found_user = User.objects.get(email=data['email'])
            if bcrypt.hashpw(data['password'].encode('utf-8'), found_user.password.encode('utf-8')) != found_user.password.encode('utf-8'):
                errors.append("Incorrect password.")
        except:
            errors.append("Entered email does not exist. (email is case sensitive)")

        if len(errors)>0:
            return{
            'logged_user':None,
            'errors_list':errors,
            }
        else:
            return{
            'logged_user':found_user,
            'errors_list':None,
            }

class BusinessManager(models.Manager):
    def register(self, data):
        errors = []
        if data['name']=="":
            errors.append("Business name may not be blank.")
        if data['city']=="":
            errors.append("City may not be blank.")
        if data['state']=="":
            errors.append("State may not be blank.")
        if data['email']=="":
            errors.append("Email address may not be blank.")
        try:
            User.objects.get(email=data['email'])
            Business.objects.get(email=data['email'])
            errors.append("Entered email already exists.")
        except:
            pass
        if not EMAIL_REGEX.match(data['email']):
            errors.append("Please enter a valid email address.")
        if len(data['password'])<8:
            errors.append("Password must be at least 8 characters long.")
        if data['password']!=data['confirm_password']:
            errors.append("Password and confirm Password do not match.")

        if len(errors)>0:
            return{
            'new':None,
            'errors_list':errors,
            }
        else:
            data['password']=bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            new_business=Business.objects.create(name=data['name'], city=data["city"], state=data['state'], email=data['email'], password=data['password'])
            return{
            'new':new_business,
            'errors_list':None,
            }

    def login(self,data):
        errors = []
        try:
            found_business = Business.objects.get(email=data['email'])
            if bcrypt.hashpw(data['password'].encode('utf-8'), found_business.password.encode('utf-8')) != found_business.password.encode('utf-8'):
                errors.append("Incorrect password.")
        except:
            errors.append("Entered email does not exist. (email is case sensitive)")

        if len(errors)>0:
            return{
            'logged_business':None,
            'errors_list':errors,
            }
        else:
            return{
            'logged_business':found_business,
            'errors_list':None,
            }


class MessageboardManager(models.Manager):
    def post(self, data):
        errors = []
        if data['title']=="":
            errors.append("Title may not be blank.")
        if data['message']=="":
            errors.append("Message may not be blank.")

        if len(errors)>0:
            return{
            'new':None,
            'errors_list':errors,
            }
        else:
            new_message=Messageboard_Message.objects.create(title=data['title'], message=data['message'], user=data['this_user'])
            return{
            'new':new_message,
            'errors_list':None,
            }
    def comment(self, data):
        errors = []
        if data['comment']=="":
            errors.append("Comment may not be blank.")

        if len(errors)>0:
            return{
            'new':None,
            'errors_list':errors,
            }
        else:
            new_comment=Messageboard_Comment.objects.create(comment=data['comment'], messageboard_message=data['this_message'], user=data['this_user'])
            return{
            'new':new_comment,
            'errors_list':None,
            }



class MeetupManager(models.Manager):
    def add(self, data):
        errors = []
        if len(data['eventname'])<3:
            errors.append("Eventname must be 3 or more characters.")
        if data['location']=="":
            errors.append("Location cannot be blank.")
        if data['description']=="":
            errors.append("Description cannot be blank.")
        if data['date']=="":
            errors.append("Meetup date cannot be blank.")
        elif datetime.datetime.strptime(data['date'], '%Y-%m-%d') <= datetime.datetime.now():
            errors.append("Meetup date must be in future.")
        if data['details']=="":
            errors.append("Details cannot be blank.")

        if len(errors)>0:
            return{
            'new':None,
            'errors_list':errors,
            }
        else:
            new_meetup=Meetup.objects.create(eventname=data['eventname'], description=data['description'], location=data['location'], date=data['date'], details=data['details'], user=data['this_user'])
            return{
            'new':new_meetup,
            'errors_list':None,
            }

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    image=models.FileField(upload_to="profile_picture", null=True, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Business(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image=models.FileField(upload_to="business_picture", null=True, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BusinessManager()




class Meetup(models.Model):
    eventname=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    details=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, related_name="meetups")
    objects=MeetupManager()

class Meetup_Like(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    meetup=models.ForeignKey(Meetup, related_name="meetup_likes")
    user=models.ForeignKey(User, related_name="meetup_likes")

class Meetup_Comment(models.Model):
    comment=models.CharField(max_length=255)
    user=models.ForeignKey(User)
    meetup=models.ForeignKey(Meetup, related_name="meetup_comments")

class Messageboard_Message(models.Model):
    title=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    image=models.FileField(upload_to="messageboard_message", null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, related_name="messageboard_messages")
    objects=MessageboardManager()

class Messageboard_Message_Like(models.Model):
    user=models.ForeignKey(User, related_name="messageboard_message_likes")
    messageboard_message=models.ForeignKey(Messageboard_Message, related_name="messageboard_message_likes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



class Messageboard_Comment(models.Model):
    comment=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, related_name="messageboard_comments")
    messageboard_message=models.ForeignKey(Messageboard_Message, related_name="messageboard_comments")
    objects=MessageboardManager()

class Messageboard_Message_View(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    messageboard_message=models.ForeignKey(Messageboard_Message, related_name="messageboard_message_views")

class Messageboard_Message_Bookmark(models.Model):
    user=models.ForeignKey(User, related_name="messageboard_message_bookmarks")
    messageboard_message=models.ForeignKey(Messageboard_Message, related_name="messageboard_message_bookmarks")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# class Deal(models.Model):
#     pass




# class Deal(models.Model):
#     name=models.CharField(max_length=255)
#     description=models.CharField(max_length=255)
#     date_to=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     user=models.ForeignKey(User, related_name="deals")









# NO LONGER BEING USED
# class MessageboardManager(models.Manager):
#     def message(self, data):
#         errors = []
#         if data['message']=="":
#             errors.append("Message may not be blank.")
#
#         if len(errors)>0:
#             return{
#             'new':None,
#             'errors_list':errors,
#             }
#         else:
#             new_message=Messageboard_Message.objects.create(message=data['message'], user=data['this_user'])
#             return{
#             'new':new_message,
#             'errors_list':None,
#             }
#
#     def comment(self, data):
#         errors = []
#         if data['comment']=="":
#             errors.append("Comment may not be blank.")
#
#         if len(errors)>0:
#             return{
#             'new':None,
#             'errors_list':errors,
#             }
#         else:
#             new_comment=Messageboard_Comment.objects.create(comment=data['comment'], user=data['this_user'], messageboard_message=data['this_message'])
#             return{
#             'new':new_comment,
#             'errors_list':None,
#             }
#
# class Messageboard_Message(models.Model):
#     message=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     user=models.ForeignKey(User, related_name="messageboard_messages")
#     objects=MessageboardManager()
#
#
# class Messageboard_Comment(models.Model):
#     comment=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     user=models.ForeignKey(User, related_name="messageboard_comments")
#     messageboard_message=models.ForeignKey(Messageboard_Message, related_name="messageboard_comments")
#     objects=MessageboardManager()
#
# class Messageboard_Comment_Like(models.Model):
#     user=models.ForeignKey(User, related_name="messageboard_comment_likes")
#     messageboard_comment=models.ForeignKey(Messageboard_Comment, related_name="messageboard_comment_likes")
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
