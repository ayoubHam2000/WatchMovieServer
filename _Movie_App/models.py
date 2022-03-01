from django.db import models

#region User Account
def get_default_profile_image():
    return "images/movies/default-movie.jpeg"

def get_profile_image_filepath(self, filename):
    return f'images/movies/{self.id}.jpeg'


class MovieModel(models.Model):
    name = models.CharField(max_length=100)
    studio = models.CharField(max_length=100)
    movieImage = models.ImageField(
        max_length=255,
        upload_to = get_profile_image_filepath, 
        null = True, 
        blank = True, 
        default = get_default_profile_image,
    )
    # save the instance of the object and then save the image
    # for that image get the object id 
    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.movieImage
            self.movieImage = None
            super(MovieModel, self).save(*args, **kwargs)
            self.movieImage = saved_image
        super(MovieModel, self).save(*args, **kwargs)