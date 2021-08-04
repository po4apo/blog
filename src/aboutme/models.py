from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=255,
                            )
    photo = models.ImageField(upload_to="images/")
    date = models.DateField()
    vk = models.URLField()
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=12,
                              )
    github = models.URLField()
    skills = models.TextField()
    about_me = models.TextField()
    education = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'





# Create your models here.
