from django.contrib import admin
from django.urls import path
from crud import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete, name='deleteit'),
    path('update/<int:id>', views.update, name='updateit')
]
