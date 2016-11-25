from django.contrib import admin
from blog.models import Contact
from .models import Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)