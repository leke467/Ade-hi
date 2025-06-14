from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class LivestockCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Livestock Categories"
    
    def __str__(self):
        return self.name

class Breed(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(LivestockCategory, on_delete=models.CASCADE, related_name='breeds')
    description = models.TextField(blank=True)
    origin = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Animal(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
        ('not_for_sale', 'Not for Sale'),
    ]
    
    HEALTH_STATUS_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='animals')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    
    # Physical Characteristics
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="Weight in kg")
    color = models.CharField(max_length=50, blank=True)
    markings = models.TextField(blank=True, help_text="Special markings or characteristics")
    
    # Health Information
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES, default='excellent')
    vaccinated = models.BooleanField(default=True)
    vaccination_date = models.DateField(null=True, blank=True)
    last_health_check = models.DateField(null=True, blank=True)
    health_notes = models.TextField(blank=True)
    
    # Sales Information
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    
    # Media
    image = models.ImageField(upload_to='animals/', blank=True, null=True)
    additional_images = models.TextField(blank=True, help_text="URLs of additional images, one per line")
    
    # Description
    description = models.TextField(help_text="Detailed description for customers")
    breeding_notes = models.TextField(blank=True, help_text="Internal breeding information")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.breed.name}"
    
    @property
    def age_in_months(self):
        from datetime import date
        today = date.today()
        return (today.year - self.date_of_birth.year) * 12 + today.month - self.date_of_birth.month
    
    @property
    def age_display(self):
        months = self.age_in_months
        if months < 12:
            return f"{months} months"
        else:
            years = months // 12
            remaining_months = months % 12
            if remaining_months == 0:
                return f"{years} year{'s' if years > 1 else ''}"
            else:
                return f"{years} year{'s' if years > 1 else ''}, {remaining_months} month{'s' if remaining_months > 1 else ''}"

class CustomerInquiry(models.Model):
    INQUIRY_TYPES = [
        ('purchase', 'Purchase Inquiry'),
        ('breeding', 'Breeding Services'),
        ('delivery', 'Delivery & Transportation'),
        ('consultation', 'Farm Consultation'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ]
    
    # Customer Information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    
    # Inquiry Details
    subject = models.CharField(max_length=20, choices=INQUIRY_TYPES)
    message = models.TextField()
    animals_interested = models.ManyToManyField(Animal, blank=True, related_name='inquiries')
    
    # Status and Follow-up
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True, help_text="Internal notes for follow-up")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Customer Inquiries"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"

class FarmSettings(models.Model):
    # Contact Information
    farm_name = models.CharField(max_length=200, default="ADE-HI Integrated Farm Limited")
    phone_primary = models.CharField(max_length=20, default="+234 123 456 7890")
    phone_secondary = models.CharField(max_length=20, blank=True)
    email_primary = models.EmailField(default="info@ade-hi.com")
    email_secondary = models.EmailField(blank=True)
    address = models.TextField(default="Lagos State, Nigeria")
    
    # Business Hours
    working_hours = models.TextField(default="Mon - Fri: 8:00 AM - 6:00 PM\nSat: 9:00 AM - 4:00 PM")
    
    # About Information
    about_description = models.TextField(default="Your trusted partner for premium quality livestock.")
    mission_statement = models.TextField(blank=True)
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    
    # Website Settings
    featured_animals_count = models.PositiveIntegerField(default=6, help_text="Number of animals to show on homepage")
    enable_online_inquiries = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Farm Settings"
        verbose_name_plural = "Farm Settings"
    
    def __str__(self):
        return self.farm_name
    
    def save(self, *args, **kwargs):
        # Ensure only one settings instance exists
        if not self.pk and FarmSettings.objects.exists():
            raise ValueError("Only one FarmSettings instance is allowed")
        super().save(*args, **kwargs)