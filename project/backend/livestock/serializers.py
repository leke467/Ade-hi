from rest_framework import serializers
from .models import LivestockCategory, Breed, Animal, CustomerInquiry, FarmSettings

class LivestockCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockCategory
        fields = ['id', 'name', 'description']

class BreedSerializer(serializers.ModelSerializer):
    category = LivestockCategorySerializer(read_only=True)
    
    class Meta:
        model = Breed
        fields = ['id', 'name', 'category', 'description', 'origin']

class AnimalSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(read_only=True)
    age_display = serializers.ReadOnlyField()
    age_in_months = serializers.ReadOnlyField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Animal
        fields = [
            'id', 'name', 'breed', 'gender', 'date_of_birth', 'age_display', 'age_in_months',
            'weight', 'color', 'markings', 'health_status', 'vaccinated', 'vaccination_date',
            'last_health_check', 'price', 'status', 'featured', 'image', 'image_url',
            'additional_images', 'description', 'created_at', 'updated_at'
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

class CustomerInquirySerializer(serializers.ModelSerializer):
    animals_interested = AnimalSerializer(many=True, read_only=True)
    animals_interested_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = CustomerInquiry
        fields = [
            'id', 'name', 'email', 'phone', 'subject', 'message',
            'animals_interested', 'animals_interested_ids', 'status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['status', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        animals_interested_ids = validated_data.pop('animals_interested_ids', [])
        inquiry = CustomerInquiry.objects.create(**validated_data)
        
        if animals_interested_ids:
            animals = Animal.objects.filter(id__in=animals_interested_ids)
            inquiry.animals_interested.set(animals)
        
        return inquiry

class FarmSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmSettings
        fields = [
            'id', 'farm_name', 'phone_primary', 'phone_secondary',
            'email_primary', 'email_secondary', 'address', 'working_hours',
            'about_description', 'mission_statement', 'facebook_url',
            'instagram_url', 'twitter_url', 'featured_animals_count',
            'enable_online_inquiries'
        ]