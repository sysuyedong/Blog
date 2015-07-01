from django.db import models

class Person(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    def __unicode__(self):
    	return self.name

class Comment(models.Model):
	commenter = models.ForeignKey("Person")
	content = models.TextField()
	comment_time = models.DateTimeField()
	def __unicode__(self):
		return self.commenter.name

class Tag(models.Model):
	tag_name = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.tag_name

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	author = models.CharField(max_length = 30)
	publish_time = models.DateTimeField()
	content = models.TextField()
	tags = models.ManyToManyField("Tag")
	def __unicode__(self):
		return self.title