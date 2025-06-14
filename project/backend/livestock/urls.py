from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('settings/', views.FarmSettingsView.as_view(), name='farm-settings'),
    path('categories/', views.LivestockCategoryListView.as_view(), name='categories'),
    path('breeds/', views.BreedListView.as_view(), name='breeds'),
    path('animals/', views.AnimalListView.as_view(), name='animals'),
    path('animals/featured/', views.FeaturedAnimalsView.as_view(), name='featured-animals'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('inquiries/', views.CustomerInquiryCreateView.as_view(), name='create-inquiry'),
]