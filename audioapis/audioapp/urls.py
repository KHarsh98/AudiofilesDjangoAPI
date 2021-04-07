from django.urls import path

from . import views

app_name= 'audioapp'

urlpatterns = [
    path('<str:filetype>/create', views.create_new, name='create'),
    path('<str:filetype>/<int:fileid>/', views.get, name ='detail'),
    path('<str:filetype>/<int:fileid>/delete', views.delete, name ='delete'),
    path('<str:filetype>/<int:fileid>/update', views.update, name ='update'),
    path('<str:filetype>/', views.get_all, name='detailAll')
]