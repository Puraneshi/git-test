from django.urls import path
from . import views

# urls here are sent to urls.py in main project folder
# the 'name' value as called by the {% url %} template tag
app_name = 'polls'
urlpatterns = [
    # polls/
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
