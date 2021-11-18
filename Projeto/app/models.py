from django.db import models

# Create your models here.
#base de dados inicial se virmos que queremos mais campos é so dar atualizar
class Groups(models.Model):
    #id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=70)

    def __str__(self):
        return self.description


class Users(models.Model):
    #ver uma função para encriptar a pass
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    password = models.CharField(max_length=50)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name +self.last_name


class Publication_status(models.Model):
    description = models.CharField(max_length=70)


    def __str__(self):
        return self.description


class Publication_topics(models.Model):
    description = models.CharField(max_length=70)


    def __str__(self):
        return self.description


class Publications(models.Model):
    title = models.CharField(max_length=70)
    content = models.CharField(max_length=200)
    creted_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    status=models.ForeignKey(Publication_status, on_delete=models.CASCADE)
    topic = models.ForeignKey(Publication_topics, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment


class Favorites(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE)
    def __str__(self):
        return self.author + self.publication


