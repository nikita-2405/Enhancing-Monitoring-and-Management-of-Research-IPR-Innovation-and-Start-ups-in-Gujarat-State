
from django.urls import path

from .views import (
    InnovationListCreateView,
    InnovationDetailView,
    innovation_page,
    add_innovation,
    edit_innovation,
    delete_innovation,
)

urlpatterns = [
    # API URLs
    path('', InnovationListCreateView.as_view(), name='innovation-list-create'),
    path('<int:pk>/', InnovationDetailView.as_view(), name='innovation-detail'),

    # Webpage URLs
    path('page/', innovation_page, name='innovation-page'),
    path('page/add/', add_innovation, name='add-innovation'),
    path('page/edit/<int:pk>/', edit_innovation, name='edit-innovation'),
    path('page/delete/<int:pk>/', delete_innovation, name='delete-innovation'),
]
