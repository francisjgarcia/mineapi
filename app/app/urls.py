from django.urls import path, include

urlpatterns = [
  path('', include('general.urls')),
  path('api/v1/', include('mineapi.urls')),
]
