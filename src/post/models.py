from django.db import models
from ckeditor.fields import RichTextField

# from post.utils import create_slug

class Image(models.Model):
    #todo: работа с изображениями пока что в жопе, фото просто не отображаются на сайте, нужно с этим позже разобраться
    name = models.CharField(max_length=255, verbose_name='Название/Описание', )
    #postID = models.ForeignKey('Post',
     #                          on_delete=models.CASCADE,
      #                         verbose_name='ID публикации')
    #numbers = models.IntegerField(verbose_name='Номер картинки в статье')
    image = models.ImageField(verbose_name='Изображение', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def image_img(self):
        if self.image:
            return u'< img src="%s" width="100"/>' % self.image.url
        else:
            return '(none)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

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
    title = models.CharField(max_length=255,
                             verbose_name='Заголовок',
                             )
    body = RichTextField(verbose_name='Текст публикации',
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

    slug = models.CharField(max_length=255,
                            blank=True,
                            unique=True,
                            verbose_name='Слаг',
                            )
    shortDescription = models.TextField(verbose_name='Краткое описание',
                                        )

    publicationDate = models.DateField(auto_now_add=True,
                                       verbose_name='Дата публикации')


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
