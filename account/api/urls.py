from django.urls import path
from rest_framework import routers

from account.api import views

router = routers.SimpleRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'employee', views.EmployeeViewSet)

urlpatterns = [
    path('person/', views.PersonAPIView.as_view(), name='person'),
    path('employee/', views.EmployeeAPIView.as_view(), name='employee'),
]

urlpatterns += router.urls
