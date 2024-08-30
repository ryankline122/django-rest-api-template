from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/items/', views.ItemViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

