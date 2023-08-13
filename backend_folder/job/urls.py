from django.urls import path
from . import views


urlpatterns = [
    path('newest/', views.NewsetJobsView.as_view()),
    path('browse/', views.BrowseJobsView.as_view()),
    path('<int:pk>/', views.JobsDetailView.as_view()),
    path('category/', views.CategoryView.as_view()),
]
