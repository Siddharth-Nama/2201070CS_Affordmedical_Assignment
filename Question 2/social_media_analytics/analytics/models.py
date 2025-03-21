from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    type = models.CharField(max_length=10, choices=[('latest', 'Latest'), ('popular', 'Popular')])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
