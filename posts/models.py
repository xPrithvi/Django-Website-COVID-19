"""Python Dependencies."""
from django.db import models

class Post(models.Model):
    """Class to contain the information/content regarding a given blog post."""
    title = models.CharField(max_length = 120) #Every post has a title.
    content = models.TextField() #The main content of the post.
    last_updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "%s/" %(self.id)
