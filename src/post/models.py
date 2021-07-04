from django.db import models

# from post.utils import create_slug


class Category(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name='Название'
                            )
    description = models.TextField(verbose_name='Описание',
                                   blank=True,
                                   )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




class Post(models.Model):
    title = models.CharField(max_length=250,
                             verbose_name='Заголовок',
                             )
    body = models.TextField(verbose_name='Текст публикации',
                            )
    publishedDate = models.DateField(auto_now_add=True,
                                     verbose_name='Дата публикации',
                                     )
    enable = models.BooleanField(verbose_name='Показать пост',
                                 )
    commentsEnable = models.BooleanField(verbose_name='Включить комментарии',
                                         )
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория',
                                 )
    # todo: add func for generate slug
    slug = models.CharField(max_length=250,
                            blank=True,
                            unique=True,
                            verbose_name='Слаг',
                            )
    shortDescription = models.TextField(verbose_name='Краткое описание',
                                        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = create_slug(self.title)
    #     super().save(*args, **kwargs)

class Coment(models.Model):
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             verbose_name='Публикиця',

                             )
    userName = models.CharField(max_length=25,
                                verbose_name='Имя пользователя',

                                )
    body = models.TextField(verbose_name='Комментарий',
                            )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.body
