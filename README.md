# Django Kit

A modern Django 6.0 starter kit with REST API, JWT authentication, and a beautiful admin interface powered by Django Unfold.

## 🚀 Features

- **Django 6.0** - Latest Django version
- **Django REST Framework** - Full-featured REST API
- **JWT Authentication** - Simple JWT implementation
- **Django Unfold** - Modern, beautiful admin interface
- **PostgreSQL Support** - Production-ready database configuration
- **Custom User Model** - Email-based authentication
- **User Profiles** - Extended user information
- **Password Reset** - OTP-based password recovery
- **Media Handling** - Image upload support with Pillow
- **Static Files** - WhiteNoise for efficient static file serving

## 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL (optional, SQLite is used by default)
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd django_kit
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

Create a `.env` file in the project root for sensitive configurations:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Seed Database with Test Users

```bash
python manage.py seed_users
```

This creates:
- **Superuser**: admin@admin.com / 12345678
- **5 Test Users**: All with password `password123`
  - john.doe@example.com
  - jane.smith@example.com
  - bob.wilson@example.com
  - alice.johnson@example.com
  - charlie.brown@example.com

### 7. Create Static Directory (if needed)

```bash
mkdir static
python manage.py collectstatic --noinput
```

### 8. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 📱 Access Points

- **Admin Panel**: http://localhost:8000/admin/
- **API Endpoints**: http://localhost:8000/api/
- **User API**: http://localhost:8000/api/users/

## 🔐 Authentication

### Obtain JWT Token

```bash
POST /api/token/
{
  "email": "admin@admin.com",
  "password": "12345678"
}
```

Response:
```json
{
  "access": "access_token_here",
  "refresh": "refresh_token_here"
}
```

### Refresh Token

```bash
POST /api/token/refresh/
{
  "refresh": "refresh_token_here"
}
```

### Use Token in Requests

```bash
Authorization: Bearer <access_token>
```

## 📁 Project Structure

```
django_kit/
├── apps/
│   ├── cms/              # CMS application
│   └── users/            # User management
│       ├── management/
│       │   └── commands/
│       │       └── seed_users.py
│       ├── models.py     # User, UserProfile, PasswordResetOTP
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
├── project/
│   ├── settings.py       # Main settings
│   ├── urls.py           # URL configuration
│   ├── asgi.py           # ASGI config
│   └── wsgi.py           # WSGI config
├── templates/            # HTML templates
├── uploads/              # Media files
├── static/               # Static files
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🛠️ Management Commands

### Create Superuser (Manual)

```bash
python manage.py createsuperuser
```

### Seed Database

```bash
python manage.py seed_users
```

### Make Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Tests

```bash
python manage.py test
```

### Collect Static Files

```bash
python manage.py collectstatic
```

## 🔧 Development

### Create a New App

```bash
python manage.py startapp app_name
cd apps/
mv ../app_name .
```

Don't forget to add the app to `INSTALLED_APPS` in `settings.py`

### Database Shell

```bash
python manage.py dbshell
```

### Django Shell

```bash
python manage.py shell
```

## 📦 Key Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0 | Web framework |
| djangorestframework | 3.16.1 | REST API |
| djangorestframework-simplejwt | 5.5.1 | JWT authentication |
| django-unfold | 0.74.1 | Modern admin UI |
| django-filter | 25.2 | Filtering support |
| psycopg2-binary | 2.9.11 | PostgreSQL adapter |
| Pillow | 12.0.0 | Image processing |
| uvicorn | 0.40.0 | ASGI server |
| whitenoise | 6.11.0 | Static file serving |

## 🚀 Production Deployment

### 1. Update Settings

- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Configure PostgreSQL database

### 2. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 3. Run with Gunicorn or Uvicorn

```bash
# Using Gunicorn (WSGI)
gunicorn project.wsgi:application --bind 0.0.0.0:8000

# Using Uvicorn (ASGI)
uvicorn project.asgi:application --host 0.0.0.0 --port 8000
```

### 4. Use a Process Manager

Consider using systemd, supervisor, or Docker to manage the application process.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- Static files directory warning on first run (create `static/` directory)
- Default SQLite database (configure PostgreSQL for production)

## 📞 Support

For issues and questions, please open an issue in the repository.

---

**Happy Coding! 🎉**
