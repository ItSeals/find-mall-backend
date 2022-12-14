from django.db import models

# Create your models here.


class Mall(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
