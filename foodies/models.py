from django.db import models



class Post(models.Model):
	user_id = models.IntegerField()
	image = models.TextField(default=None)
	title = models.CharField(max_length = 75)
	def __str__(self):
		return self.title


