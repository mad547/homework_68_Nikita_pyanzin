from django.urls import path
from webapp.views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('calculator/', IndexView.as_view(), name='index'),
]