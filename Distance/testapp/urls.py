from django.urls import path
from testapp import views

app_name = 'testapp'
urlpatterns = [
    path('', views.calculate_distance_view,name="calculate-view"),
]
