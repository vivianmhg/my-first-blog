from django.contrib import admin
from .models import Post #import Post from the models you created

admin.site.register(Post) #allow it to be visible on admin page
