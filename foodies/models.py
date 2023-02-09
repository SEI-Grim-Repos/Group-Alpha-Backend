from django.db import models

COUNTRIES_LIST = ['List of All Countries']

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
	date = models.DateField.auto_now_add
	image = models.FileField()
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
    post_id = models.IntegerField()
    body = models.TextField()
    post= models.ForeignKey(
        Post,
        on_delete= models.CASCADE,
        default= None
    )
    def __str__ (self):
        return self.body
