from django.contrib import admin
from .models import Genre, Movie, Actor, Directory

admin.site.register([Genre, Movie, Actor, Directory,])