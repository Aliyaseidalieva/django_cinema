from django.contrib import admin

from .models import Genre, Movie, MovieShots, Actor, Review, File

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(File)


