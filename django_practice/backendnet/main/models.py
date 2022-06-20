from django.db import models
from random import randint


link_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_", "!"]

tags_ = [
    ("python / django", "python / django"),
    ("php", "php"),
    ("java", "java"),
    ("ruby", "ruby"),
    ("js / js frameworks", "js / js frameworks"),
    ("linux / server operation", "linux / server operation"),
    ("databases", "databases"),
    ("metapost", "metapost"),
    ("tips and tricks", "tips and tricks"),
    ("workflow", "workflow"),
    ("etc", "etc"),
]

def make_link():
    link_ = []
    for _ in range(30):
        link_.append(link_chars[randint(0, 63)])
    return "".join(link_)


class Article(models.Model):
    # article_author = request.user.username()
    article_author  = models.CharField(max_length=12)
    article_name    = models.CharField(max_length=60)
    article_body    = models.TextField()
    article_date    = models.DateTimeField(auto_now_add=True)
    article_tags    = models.CharField(max_length=25, choices=tags_, null=True)
    # article_link    = models.SlugField(make_link(), unique=True)
    # article_link    = make_link()

    def snippet(self):
        return self.article_body[:150]

    def __str__(self):
        return self.article_name


# Create your models here.
