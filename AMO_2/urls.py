from django.contrib import admin
from django.urls import path, include

from algorithms.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('algortihms/', include('algorithms.urls', namespace='algorithms')),
    path('', home_view)
]
