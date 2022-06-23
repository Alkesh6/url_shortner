from cgi import test
from django.contrib import admin
from django.urls import include, path
from . import views

# urlpatterns = [
#     # path('hello', views.hello)
# ]
urlpatterns = [
    path('',views.homePage),
    path('test',views.test),
    path('all-analytics',views.all_analytics),
    path('<slug:short_url>',views.redirect_url)
]