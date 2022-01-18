from django.db import models

# Create your models here.




class Groups(models.Model):
    description = models.CharField(max_length=70)

    def __str__(self):
        return self.description

if len(Groups.objects.all()) == 0:
    group = Groups(description='Admin')
    group.save()
    group = Groups(description='Leitor')
    group.save()
    group = Groups(description='Gestor')
    group.save()
    group = Groups(description='Autor')
    group.save()
class Publication_status(models.Model):
    description = models.CharField(max_length=70)


    def __str__(self):
        return self.description

if len(Publication_status.objects.all()) == 0:
    group = Publication_status(description='Arquivado')
    group.save()
    group = Publication_status(description='Por Aprovar')
    group.save()
    group = Publication_status(description='Aprovado')
    group.save()


class Publication_topics(models.Model):
    description = models.CharField(max_length=70)


    def __str__(self):
        return self.description


class Users(models.Model):
    username = models.CharField(max_length=70,default="")
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Publications(models.Model):
    title = models.CharField(max_length=70)
    content = models.CharField(max_length=20000)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.ForeignKey(Publication_status, on_delete=models.CASCADE)
    topic = models.ForeignKey(Publication_topics, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Comments(models.Model):
    comment = models.CharField(max_length=300)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

class Favorites(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)

