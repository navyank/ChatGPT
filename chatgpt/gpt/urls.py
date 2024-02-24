
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('response', views.chat_with_gpt, name='response'),
    path('history',views.chat_history,name="history"),
    path('clear',views.clear_history,name='clear')
]