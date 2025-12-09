"""
URL configuration for satellite_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from tracker.views import SatelliteTrackerView

def home(request):
    """
    Home page with API documentation
    """
    api_info = {
        'message': 'Satellite Tracking API',
        'description': 'Real-time satellite tracking using SGP4 algorithm',
        'endpoints': {
            'satellites_list': '/api/satellites/',
            'satellite_detail': '/api/satellites/<norad_id>/',
        },
        'examples': {
            'satellites_list': 'http://localhost:8000/api/satellites/',
            'iss_tracking': 'http://localhost:8000/api/satellites/25544/'
        }
    }
    return JsonResponse(api_info)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/satellites/', SatelliteTrackerView.as_view(), name='satellites-list'),
    path('api/satellites/<int:norad_id>/', SatelliteTrackerView.as_view(), name='satellite-detail'),
]
