from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import LivestockCategory, Breed, Animal, CustomerInquiry, FarmSettings
from .serializers import (
    LivestockCategorySerializer, BreedSerializer, AnimalSerializer,
    CustomerInquirySerializer, FarmSettingsSerializer
)

class LivestockCategoryListView(generics.ListAPIView):
    queryset = LivestockCategory.objects.all()
    serializer_class = LivestockCategorySerializer

class BreedListView(generics.ListAPIView):
    queryset = Breed.objects.select_related('category')
    serializer_class = BreedSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class AnimalListView(generics.ListAPIView):
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        queryset = Animal.objects.select_related('breed__category').filter(
            status__in=['available', 'reserved']
        )
        
        # Filter parameters
        breed_id = self.request.query_params.get('breed', None)
        category_id = self.request.query_params.get('category', None)
        status = self.request.query_params.get('status', None)
        featured = self.request.query_params.get('featured', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        search = self.request.query_params.get('search', None)
        
        if breed_id:
            queryset = queryset.filter(breed_id=breed_id)
        
        if category_id:
            queryset = queryset.filter(breed__category_id=category_id)
        
        if status:
            queryset = queryset.filter(status=status)
        
        if featured is not None:
            queryset = queryset.filter(featured=featured.lower() == 'true')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(breed__name__icontains=search) |
                Q(description__icontains=search)
            )
        
        return queryset.order_by('-featured', '-created_at')

class AnimalDetailView(generics.RetrieveAPIView):
    queryset = Animal.objects.select_related('breed__category')
    serializer_class = AnimalSerializer

class FeaturedAnimalsView(generics.ListAPIView):
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        settings = FarmSettings.objects.first()
        limit = settings.featured_animals_count if settings else 6
        
        return Animal.objects.select_related('breed__category').filter(
            featured=True,
            status__in=['available', 'reserved']
        ).order_by('-created_at')[:limit]

class CustomerInquiryCreateView(generics.CreateAPIView):
    queryset = CustomerInquiry.objects.all()
    serializer_class = CustomerInquirySerializer

class FarmSettingsView(generics.RetrieveAPIView):
    serializer_class = FarmSettingsSerializer
    
    def get_object(self):
        settings, created = FarmSettings.objects.get_or_create(
            defaults={
                'farm_name': 'ADE-HI Integrated Farm Limited',
                'phone_primary': '+234 123 456 7890',
                'email_primary': 'info@ade-hi.com',
                'address': 'Lagos State, Nigeria',
                'about_description': 'Your trusted partner for premium quality livestock.',
            }
        )
        return settings

@api_view(['GET'])
def api_overview(request):
    """
    API Overview - Available endpoints
    """
    api_urls = {
        'Farm Settings': '/api/settings/',
        'Categories': '/api/categories/',
        'Breeds': '/api/breeds/',
        'All Animals': '/api/animals/',
        'Featured Animals': '/api/animals/featured/',
        'Animal Detail': '/api/animals/<id>/',
        'Submit Inquiry': '/api/inquiries/',
        'API Overview': '/api/',
    }
    return Response(api_urls)