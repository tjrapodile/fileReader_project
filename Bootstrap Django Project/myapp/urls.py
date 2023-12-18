from django.urls import path
from .views import upload_csv,upload_success,arima_models_view,index,analysis

urlpatterns = [
    path('index/', index, name='index'),
    path('index/upload_csv.html/', upload_csv, name='upload_csv'),
    path('index/upload_csv.html/upload_success.html/', upload_success, name='upload_success'),
    path('index/upload_success.html/', upload_success, name='upload_success'),
     path('index/upload_csv.html/upload_success.html/arima_models_view.html/', arima_models_view, name='arima_models_view'),
    path('index/arima_models_view.html/', arima_models_view, name='arima_models_view'),
    path('index/analysis.html/', analysis, name='analysis'),
]



