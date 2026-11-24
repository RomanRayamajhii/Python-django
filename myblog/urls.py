from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name="about"),
    path('user/<str:username>/',views.user,name="user"),
    path('post/<str:post_id>/',views.post,name="post")
]