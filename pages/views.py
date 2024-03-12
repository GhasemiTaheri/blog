from django.views.generic import CreateView, ListView

from pages.models import Article
from utils.helper import RedirectToIndexMixin


class CreateArticleView(RedirectToIndexMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'author', 'category']
    template_name = 'pages/create_article.html'


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'pages/article_list.html'
