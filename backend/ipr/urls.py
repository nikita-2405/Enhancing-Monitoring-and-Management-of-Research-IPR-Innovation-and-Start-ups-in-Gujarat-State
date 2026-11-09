
from django.urls import path
from .views import (
    IPRListCreateView,
    IPRDetailView,
    ipr_page,
    add_ipr,
    edit_ipr,
    delete_ipr,
)

urlpatterns = [
    # Existing API routes
    path('', IPRListCreateView.as_view(), name='ipr-list-create'),
    path('<int:pk>/', IPRDetailView.as_view(), name='ipr-detail'),

    # IPR webpage routes
    path('page/', ipr_page, name='ipr-page'),
    path('page/add/', add_ipr, name='add-ipr'),
    path('page/edit/<int:pk>/', edit_ipr, name='edit-ipr'),
    path('page/delete/<int:pk>/', delete_ipr, name='delete-ipr'),
]
