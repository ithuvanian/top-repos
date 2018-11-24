from django.db import models

# Create your models here.


class Languages(models.Model):
    list = {
        'python': 'python.png',
        'ruby': 'ruby.png',
        'elixir': 'elixir.png',
        'css': 'css.png',
        'javascript': 'javascript.png',
        'c#': 'csharp.png',
        'java': 'java.png',
        'rust': 'rust.png'
    }


class RepoSummary(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    stars = models.IntegerField()
    description = models.TextField()
