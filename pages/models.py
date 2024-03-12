from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE,
                               related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 related_name='articles')


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
