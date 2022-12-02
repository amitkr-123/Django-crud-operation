from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='home'),
    path('add', views.add),
    path('remove/<int:id>', views.remove),
    path('edit/<int:id>' , views.edit),
    path('update/<int:id>' , views.update)
]