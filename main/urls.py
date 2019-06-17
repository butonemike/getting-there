from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('lines/', views.lines_index, name='lines_index'),
    path('lines/<int:line_id>/', views.lines_detail, name='lines_detail'),
    path('trips/new/<int:line_id>/<int:station_id>/', views.trips_new, name='trips_new'),
    # path('trips/new/<int:line_id>/<int:station_id>/', views.TripCreate.as_view(), name='trip_create'),
    path('trips/edit/', views.trips_edit, name='trips_edit'),
]
