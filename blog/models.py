from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True, blank=True)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/blog')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="blog")
    tag = models.ManyToManyField("Tag", related_name="blog", blank=True, null=True)


    class Meta:
        ordering = ('created_at',)
        

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)



class Comment(models.Model):
    blog = models.ForeignKey("Blog", related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name