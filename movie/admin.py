from django.contrib import admin
from .models import Movie, MovieLinks, Rating
# from .models import Movie, MovieLinks, Tvshow, TvshowLinks

# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieLinks)

# admin.site.register(Tvshow)
# admin.site.register(TvshowLinks)

admin.site.register(Rating)
