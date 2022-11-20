from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    #add in thumbnail later
    # add in author later

# __str__() built in function which defines an article will look like both the admin session and the pyton shell when retrive the objects
    def __str__(self):
      return self.title
    
    def snippet(self):
        return self.body[:50] + '...'

      