from django.conf.urls import url
from appTwo import views
from django.urls import path
from django.contrib.auth import views as auth_views
# from rest_framework.authtoken import obtain_auth_token

urlpatterns=[
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('upload/',views.uploadFile,name='upload'),
    path('search/',views.searchInfo,name='search'),
    path('create/',views.create,name="create"),
    path('read/',views.read,name="read"),
    path('edit/', views.edit),  
    path('update/<str:name>', views.update),  
    path('delete/<str:name>', views.delete),
    path('register', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='appTwo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appTwo/logout.html'), name='logout'),
    #path(r'^profiles/home', appTwo/home.html),
    path('authenticate/', views.CustomObtainAuthToken.as_view()),
    # path('login',obtain_auth_token,name="login")
    path('items/', views.item_list),
    path('item/<str:pk>/', views.item_detail),
]