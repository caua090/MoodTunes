
from django.contrib import admin
from django.urls import path
from Meu_APP.views import home, recomendar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('recomendar/', recomendar, name='recomendar'),
]
