from django.urls import path, include

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    # Додайте інші шляхи при необхідності
]
