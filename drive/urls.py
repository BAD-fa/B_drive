from django.urls import path

from .views import Login, Upload, logout, show_files, home


app_name = 'drive'

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('my-files/', show_files, name="show_files"),
    path('upload/', Upload.as_view(), name='upload'),
    path('logout/', logout, name='logout')
]
