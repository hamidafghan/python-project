from django.urls import path
from . import views
urlpatterns = [
    # path
    path('', views.welcome),
    path('contact-us/', views.contact_us),
    path('about-us/', views.about_us),
    path('years/<int:year>/', views.year)
]
