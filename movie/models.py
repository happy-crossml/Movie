from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.

# Choices for the 'category' field in the Movie model
CATEGORY_CHOICES = (
    ('action', 'ACTIONS'),
    ('drama', 'DRAMA',),
    ('comedy', 'COMEDY')
)

# Choices for the 'language' field in the Movie model

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('hindi', 'HINDI')
)

# Choices for the 'status' field in the Movie model
STATUS_CHOICES = (
    ('RA', 'RECENTLY'),
    ('MW', 'MOST WATCHES'),
    ('TR', 'TOP RATED'),    
    ('CS', 'COMING SOON'),
)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner=models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    years_of_production = models.DateField()
    cast = models.CharField(max_length=250)
    movie_trailer = models.URLField()
    slug = models.SlugField(blank=True, null=True)
    
    # Generate slug from the title using the slugify function
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Movie, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

# Choices for the 'type' field in the MovieLinks model
LINK_CHOICES = (
    ('W', 'WATCH LINK'),
    ('D', 'DOWNLOAD LINK')
)
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie) + ' ' + str(self.movie) # Return the string representation of the object
    

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return str(self.rate) # Return the string representation of the object
