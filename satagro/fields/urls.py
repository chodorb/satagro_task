from django.urls import path
from fields.views import FieldDetailAPIView, FieldTechlinesDetailAPIView

urlpatterns = [
    path('/<str:pk>',FieldDetailAPIView.as_view()),
    path('/<str:pk>/techlines',FieldTechlinesDetailAPIView.as_view())
]
