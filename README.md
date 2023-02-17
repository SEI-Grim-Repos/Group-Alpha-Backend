# Group-Alpha-Backend

 This is the backend for our gourmet gather applicaiton (Team of nine). In this back end we had to create a table and model for our projects and deploy it on heroku.

### Built with

    DJANGO (pip install django)
    PYTHON
    SQL
---
### Installations

    virtual environment
    psycopg2-binary
    djangorestframework

    To install all installations 

        pip install -r requirements.txt
---

### What we did 

Create a virtual environment (terminal)

    mkvirtualenv group_alpha_backend

Create branch to work in (since we won't have merge conflicts) (terminal)

    git checkout -b backend-basics

Install django (terminal)

    pip install django

Get into the environment (it will automatically move you in there) (terminal)

    workon .

Freeze and create requirements.txt (freeze gives a list of your installed dependencies) (terminal)

    pip freeze > requirements.txt

Create our project folder called group_alpha_backend (DONT FORGET THE PERIOD !!)(terminal)

    django-admin startproject group_alpha_backend .

Install pyscopg2-binary (terminal)

    pip install psycopg2-binary

make a sql file (To make the table, username and password in the backend) (terminal)

    touch create-database.sql

In create-database.sql file

    CREATE DATABASE food;

    CREATE USER group_alpha_backend_admin WITH PASSWORD 'password';

    GRANT ALL PRIVILEGES ON DATABASE  TO group_alpha_backend_admin;

Now we need to run migrations to basically save what we added ( this may not work until we add an admin for our app and make a password) (the first one checks what changes were added and the second one implements the changes in the live server) (terminal)

    python manage.py makemigrations 

then (terminal)

    python manage.py migrate

(make user super user code below) you can check if the table was created with \d (in psql)(terminal)

    alter role group_alpha_backend_admin with superuser;

go to line 76 in settings.py to change to the following 
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'food',
        'USER': 'group_alpha_backend_admin',
        'PASSWORD': 'password',
        'HOST': 'localhost'
        }
    }

Now run the server to see if we run into any issues (terminal) 

SERVER SHOULD BE RUNNING AFTER RUNNING THE CODE BELOW

    python manage.py runserver


Create an app inside of projects (terminal)

    django-admin startapp foodies

In line 33 add the sudents app to the settings.py (what it should look like)   

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'foodies'
    ]

Create model in the models.py in the student folder (what t should look like)

    from django.db import models
    import datetime

    COUNTRIES_LIST = [ **Actual list of countries, check the models.py file to see it
    ]

    class User(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 32)
    location = models.CharField(
		max_length = 20,
		choices = COUNTRIES_LIST,
	    default = None
	)
    def __str__(self):
	    return self.username


    class Post(models.Model):
        user_id = models.IntegerField()
        date = models.DateField.auto_now_add= True
        image = models.TextField(default=None)
        title = models.CharField(max_length = 75)
        body = models.TextField()
        location = models.CharField(
            max_length = 20,
            choices = COUNTRIES_LIST,
            default = None
        )
        likes = models.IntegerField()
        
        def __str__(self):
            return self.title


    class Comment(models.Model):
        user_id = models.IntegerField()

        # post_id = models.IntegerField()
        body = models.TextField()
        post= models.ForeignKey(
            Post,
            on_delete= models.CASCADE,
            default= None
        )
        def __str__ (self):
            return self.body


Make mirgrations (terminal)
 
    python manage.py makemigrations

    python manage.py migrate

Look at db (psql) (terminal)

    \c foods (foods is the name of the database)

    \d (lists everything in the db) (exit it by typing q)

check to see if our server is giving us an errors (on web) (python manage.py runserver)

we need to register our models (foodies/admin.py)

    from django.contrib import admin
    from .models import User, Post, Comment

    admin.site.register(User)
    admin.site.register(Post)
    admin.site.register(Comment)


create superuser (terminal)

    python manage.py createsuperuser
 
    us: group_alpha_backend_admin
    email:
    pw: 123

now lets run admin in the url (localhost:8000/admin)


### NOW LETS DO REST

in virtual env  (reminder: workon .) (terminal)

    pip install djangorestframework

    pip freeze > requirements.txt

make sure you add the rest framework of the dependencies in the intalled apps in the settings.py

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'foodies',
        'rest_framework'
    ]

make a file called serializers.py
    
    touch students/ serializers.py

and add this 

    from rest_framework import serializers
        
    from .models import User, Comment, Post

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'


    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = '__all__'

OPEN  foodies/views.py 
remove django default method bc we want to see json

    from rest_framework import viewsets

    from .serializers import UserSerializer, CommentSerializer, PostSerializer
    from .models import User, Comment, Post

    class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        
    class CommentViewSet(viewsets.ModelViewSet):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer

    class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer

we need to say which view set is associated with which endpoint. That's done inside of django_api_lab/urls.py

    from django.contrib import admin
    from django.urls import path, include

    from rest_framework import routers
    from foodies.views import UserViewSet, PostViewSet, CommentViewSet


    router = routers.DefaultRouter()
    router.register(r'User', UserViewSet)
    router.register(r'Post', PostViewSet)
    router.register(r'Comment', CommentViewSet)


    urlpatterns = [
        path('', include(router.urls)),
        path('admin/', admin.site.urls),
    ]




now lets check to see if the routes work
 
    http://localhost:8000/User
    http://localhost:8000/Post
    http://localhost:8000/Comment





### Problems
 
 We had problems with deploying on back end with heroku and forgetting to migrate our changes after changing anything. 
