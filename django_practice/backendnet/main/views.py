from django.shortcuts import render
from .models import Article
from .models import tags_


# Create your views here.
def home(request):
    context = {
        'title': 'backend.net',
        'Article': Article.objects.all().order_by('article_date'),
        'article_tags': tags_,
    }
    return render(request, 'index.html', context)


def article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)

































