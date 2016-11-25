from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):

    class Meta: #include this to ensure build IDE
        app_label = "blog"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=255, default=30)

class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image1 = models.ImageField(upload_to="images", blank=True, null=True)
    image2 = models.ImageField(upload_to="images", blank=True, null=True)
    image3 = models.ImageField(upload_to="images", blank=True, null=True)
    image4 = models.ImageField(upload_to="images", blank=True, null=True)
    image5 = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title