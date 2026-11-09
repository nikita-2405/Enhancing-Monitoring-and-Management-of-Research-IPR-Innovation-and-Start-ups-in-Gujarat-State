
from django.urls import path

from .views import (
    StartupListCreateView,
    StartupDetailView,
    startup_page,
    add_startup,
    edit_startup,
    delete_startup,
)

urlpatterns = [
    # Existing API routes
    path('', StartupListCreateView.as_view(), name='startup-list-create'),
    path('<int:pk>/', StartupDetailView.as_view(), name='startup-detail'),

    # Startup webpage routes
    path('page/', startup_page, name='startup-page'),
    path('page/add/', add_startup, name='add-startup'),
    path('page/edit/<int:pk>/', edit_startup, name='edit-startup'),
    path('page/delete/<int:pk>/', delete_startup, name='delete-startup'),
]
