
from django.urls import path
from .views import (
    ResearchProjectListCreateView,
    ResearchProjectDetailView,
    research_page,
    add_research,
    edit_research,
    delete_research,
)

urlpatterns = [
    # API URLs
    path('research/', ResearchProjectListCreateView.as_view(), name='research-list-create'),
    path('research/<int:pk>/', ResearchProjectDetailView.as_view(), name='research-detail'),

    # Webpage URLs
    path('projects/', research_page, name='research-page'),
    path('projects/add/', add_research, name='add-research'),
    path('projects/edit/<int:pk>/', edit_research, name='edit-research'),
    path('projects/delete/<int:pk>/', delete_research, name='delete-research'),
]
