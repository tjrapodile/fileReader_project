from django.urls import path
from .views import upload_csv,upload_success,arima_models_view

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('upload_success/', upload_success, name='upload_success'),
    path('arima_models_view.html', arima_models_view, name='arima_models_view'),
]



