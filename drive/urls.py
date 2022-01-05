from django.urls import path

from .views import Login, Upload, logout, show_my_files, show_subs_files


app_name = 'drive'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('my-files/', show_my_files, name="show_my_files"),
    path('my-files/', show_subs_files, name="show_subs_files"),
    path('upload/', Upload.as_view(), name='upload'),
    path('logout/', logout, name='logout')
]
