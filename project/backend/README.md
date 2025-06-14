# ADE-HI Farm Backend

Django REST API backend for ADE-HI Integrated Farm Limited website.

## Features

- **Admin Panel**: Complete Django admin interface for managing livestock
- **REST API**: Full API for frontend integration
- **Animal Management**: Track animals with detailed information (weight, age, health, etc.)
- **Customer Inquiries**: Handle customer contact forms and inquiries
- **Image Upload**: Support for animal photos
- **Farm Settings**: Configurable farm information and contact details

## Setup Instructions

1. **Install Python Dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Admin User**:
   ```bash
   python manage.py createsuperuser
   ```

4. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access Admin Panel**:
   - URL: http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

## API Endpoints

- `GET /api/` - API overview
- `GET /api/settings/` - Farm settings and contact info
- `GET /api/categories/` - Livestock categories
- `GET /api/breeds/` - Animal breeds
- `GET /api/animals/` - All available animals
- `GET /api/animals/featured/` - Featured animals for homepage
- `GET /api/animals/<id>/` - Individual animal details
- `POST /api/inquiries/` - Submit customer inquiry

## Admin Panel Features

### Animal Management
- Add/edit animals with complete details
- Upload photos for each animal
- Track health status and vaccination records
- Set pricing and availability status
- Feature animals on homepage
- Bulk actions for status updates

### Customer Inquiries
- View all customer inquiries
- Track inquiry status and follow-up
- Link inquiries to specific animals
- Add internal notes for team communication

### Farm Settings
- Update contact information
- Modify business hours
- Set social media links
- Configure website settings

## Models

### Animal
- Basic info: name, breed, gender, date of birth
- Physical: weight, color, markings
- Health: status, vaccination records, health notes
- Sales: price, availability status, featured flag
- Media: primary image and additional photos

### Customer Inquiry
- Customer contact information
- Inquiry type and message
- Animals of interest
- Status tracking and admin notes

### Farm Settings
- Contact information and business hours
- About description and mission statement
- Social media links
- Website configuration options

## Usage Tips

1. **Adding Animals**: Use the admin panel to add new animals with complete information
2. **Managing Inquiries**: Check customer inquiries regularly and update status
3. **Featured Animals**: Mark your best animals as "featured" to show on homepage
4. **Bulk Operations**: Use admin actions to update multiple animals at once
5. **Image Management**: Upload high-quality photos to attract customers

The backend is now ready to power your farm website with a professional admin interface!