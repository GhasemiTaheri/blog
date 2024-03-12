from django.urls import path

from pages.views import CreateArticleView, ArticleListView

app_name = 'pages'
urlpatterns = [
    path('add-article/', CreateArticleView.as_view(), name='create_article'),
    path('list-article/', ArticleListView.as_view(), name='list_article'),
]
