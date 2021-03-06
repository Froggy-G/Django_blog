from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Название статьи' ,max_length=200)
    text = models.TextField('Тест статьи')
    created_date = models.DateTimeField('Дата написания', default=timezone.now)
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title