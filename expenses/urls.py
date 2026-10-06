from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('budget/', views.add_budget_view, name='add_budget'),
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
]