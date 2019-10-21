from django.urls import path
from . import views
app_name='first_app'
urlpatterns = [
    # path('',views.index,name='index'),
    path('webdetails/',views.webdetails,name='webdetails'),
    path('registration/',views.register,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special_welcome,name='special'),
]
