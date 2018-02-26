from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bookZone import views

urlpatterns = [
	path('', views.index, name='index'),
	path('category', views.category, name='category'),
	path('category/<int:category_id>/', views.book, name='book'),
	path('<int:category_id>', views.book, name='book'),
	path('authors', views.author, name='authors'),
	path('authors/<int:id>', views.author, name='author'),
	path('authors/<str:follow>/<int:author_id>', views.follow, name='follow')
]

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]