from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser








class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    photo = models.ImageField(upload_to="user_post/",null=True, blank=True)
    famous = models.BooleanField(default=False)

    def __str__(self):
        
        return self.user.username


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()






class Post(models.Model):
    
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # text = models.TextField(max_length=400,blank=True,null=True)
    text= RichTextField()
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['date']   
    
    def __str__(self) :
        return f'{self.author}  | post'


# @receiver(post_save, sender=User)
# def create_post(sender, instance, created, **kwargs):
#     if created:
#         Post.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_post(sender, instance, **kwargs):
#     instance.Post.save()

