from django.db import models

# Create your models here.


class Mall(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Categories(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        
class Item(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    item_image = models.ImageField(blank=True, null=True, upload_to='image_download/')
    malls = models.ManyToManyField(Mall)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
