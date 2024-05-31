from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone


# Create your models here.

class CreateBlog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    intro=models.TextField(default='')
    body = models.TextField()
    image=models.ImageField(upload_to='media', default='' )
    date_created = models.DateTimeField(default=timezone.now)

    class Meta :
        ordering=['date_created']

class Comment(models.Model):
    post= ForeignKey(CreateBlog,related_name='comments',on_delete=models.CASCADE)
    email=models.EmailField(default='')
    body=models.TextField(default='')
    name=models.CharField(max_length=100,default="inconnu")
    date_added=models.DateTimeField(auto_now=True)

    class Meta :
        ordering=['-date_added']
        


class Memoire(models.Model):
    student_name = models.CharField(max_length=200)
    filiere = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    file = models.FileField(upload_to='memoires/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.theme
    
class Personnel(models.Model):
    nom= models.CharField(max_length=200)
    photo= models.ImageField(upload_to='media',default='')
    poste= models.CharField(max_length=200)
    
    def __str__(self):
        return self.nom
    
class Contact(models.Model):
    objet=models.CharField(max_length=200)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    tel=models.CharField(max_length=20)
    message=models.TextField()
    
    def __str__(self):
        return f"Message de {self.nom}"