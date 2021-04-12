from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailViews.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateViews.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteViews.as_view(), name='news_delete')
]