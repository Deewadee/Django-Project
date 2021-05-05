from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('index/', include('main.urls')),
    path('allspec/', include('main.urls')),
    path('my_notes/', include('main.urls')),
    path('about_company/', include('main.urls')),
    path('contacts/', include('main.urls')),

]
