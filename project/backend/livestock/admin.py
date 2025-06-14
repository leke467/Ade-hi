from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import LivestockCategory, Breed, Animal, CustomerInquiry, FarmSettings

@admin.register(LivestockCategory)
class LivestockCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'breed_count', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']
    
    def breed_count(self, obj):
        return obj.breeds.count()
    breed_count.short_description = 'Number of Breeds'

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'origin', 'animal_count', 'created_at']
    list_filter = ['category', 'origin']
    search_fields = ['name', 'description', 'origin']
    readonly_fields = ['created_at']
    
    def animal_count(self, obj):
        return obj.animals.count()
    animal_count.short_description = 'Number of Animals'

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'gender', 'age_display', 'weight', 'price', 'status', 'health_status', 'featured', 'image_preview']
    list_filter = ['status', 'health_status', 'gender', 'breed__category', 'breed', 'featured', 'vaccinated']
    search_fields = ['name', 'breed__name', 'description']
    readonly_fields = ['created_at', 'updated_at', 'age_display', 'age_in_months', 'image_preview']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'breed', 'gender', 'date_of_birth', 'age_display')
        }),
        ('Physical Characteristics', {
            'fields': ('weight', 'color', 'markings')
        }),
        ('Health Information', {
            'fields': ('health_status', 'vaccinated', 'vaccination_date', 'last_health_check', 'health_notes')
        }),
        ('Sales Information', {
            'fields': ('price', 'status', 'featured')
        }),
        ('Media', {
            'fields': ('image', 'image_preview', 'additional_images')
        }),
        ('Description', {
            'fields': ('description', 'breeding_notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', obj.image.url)
        return "No image"
    image_preview.short_description = 'Image Preview'
    
    actions = ['mark_as_available', 'mark_as_reserved', 'mark_as_sold', 'feature_animals', 'unfeature_animals']
    
    def mark_as_available(self, request, queryset):
        queryset.update(status='available')
        self.message_user(request, f"{queryset.count()} animals marked as available.")
    mark_as_available.short_description = "Mark selected animals as available"
    
    def mark_as_reserved(self, request, queryset):
        queryset.update(status='reserved')
        self.message_user(request, f"{queryset.count()} animals marked as reserved.")
    mark_as_reserved.short_description = "Mark selected animals as reserved"
    
    def mark_as_sold(self, request, queryset):
        queryset.update(status='sold')
        self.message_user(request, f"{queryset.count()} animals marked as sold.")
    mark_as_sold.short_description = "Mark selected animals as sold"
    
    def feature_animals(self, request, queryset):
        queryset.update(featured=True)
        self.message_user(request, f"{queryset.count()} animals featured on homepage.")
    feature_animals.short_description = "Feature selected animals on homepage"
    
    def unfeature_animals(self, request, queryset):
        queryset.update(featured=False)
        self.message_user(request, f"{queryset.count()} animals removed from homepage.")
    unfeature_animals.short_description = "Remove selected animals from homepage"

@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject', 'status', 'created_at']
    list_filter = ['subject', 'status', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('subject', 'message', 'animals_interested')
        }),
        ('Status & Follow-up', {
            'fields': ('status', 'admin_notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    filter_horizontal = ['animals_interested']
    
    actions = ['mark_as_contacted', 'mark_as_in_progress', 'mark_as_completed']
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
        self.message_user(request, f"{queryset.count()} inquiries marked as contacted.")
    mark_as_contacted.short_description = "Mark selected inquiries as contacted"
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
        self.message_user(request, f"{queryset.count()} inquiries marked as in progress.")
    mark_as_in_progress.short_description = "Mark selected inquiries as in progress"
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, f"{queryset.count()} inquiries marked as completed.")
    mark_as_completed.short_description = "Mark selected inquiries as completed"

@admin.register(FarmSettings)
class FarmSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact Information', {
            'fields': ('farm_name', 'phone_primary', 'phone_secondary', 'email_primary', 'email_secondary', 'address')
        }),
        ('Business Information', {
            'fields': ('working_hours', 'about_description', 'mission_statement')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url')
        }),
        ('Website Settings', {
            'fields': ('featured_animals_count', 'enable_online_inquiries')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def has_add_permission(self, request):
        # Only allow one settings instance
        return not FarmSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of settings
        return False

# Customize admin site
admin.site.site_header = "ADE-HI Farm Administration"
admin.site.site_title = "ADE-HI Farm Admin"
admin.site.index_title = "Welcome to ADE-HI Farm Administration"