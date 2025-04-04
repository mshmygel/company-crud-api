# Company CRUD API

Company CRUD API is a Django + Django REST Framework project that allows creating, retrieving, updating, and deleting company records. Each company can be associated with multiple users, and each user can belong to multiple companies. The project also includes an admin panel enhanced with Jazzmin, interactive API documentation with Swagger and Redoc, and a PostgreSQL database managed through Docker.

## Features

- Full CRUD operations for companies and users  
- Many-to-many relationship between companies and users  
- Custom user model (based on AbstractUser)  
- API documentation with Swagger and Redoc (drf-spectacular)  
- Admin panel styled with Jazzmin  
- Debugging with Django Debug Toolbar  
- Dockerized for easy local development  
- Unit tests with Pytest and coverage reporting

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/company-crud-api.git
   cd company-crud-api
   ```

2. **Install dependencies using Poetry:**
   ```bash
   poetry install
   ```

3. **Run the project with Docker:**
   ```bash
   docker-compose up --build
   ```

4. **Run migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## API Documentation

- Swagger UI: [http://localhost:8000/api/docs/swagger/](http://localhost:8000/api/docs/swagger/)  
- Redoc: [http://localhost:8000/api/docs/redoc/](http://localhost:8000/api/docs/redoc/)  
- OpenAPI schema: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## Admin Panel

Visit [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with your superuser credentials.

## Endpoints

- `/api/companies/` - List, create, retrieve, update, delete companies  
- `/api/users/` - List, create, retrieve, update, delete users  

## Testing

The project uses **pytest** and **pytest-django** for testing.

### Run tests
```bash
docker exec -it company-crud-api-web-1 pytest
```

### Run tests with coverage report
```bash
docker exec -it company-crud-api-web-1 pytest --cov=. --cov-report=term-missing
```

### Test structure
Tests are organized by app:
```
accounts/
  tests/
    test_models.py
    test_views.py
companies/
  tests/
    test_models.py
    test_views.py
```

### Fixtures
Reusable test data is defined in a shared `conftest.py` file located at the project root. This includes:

- `api_client`: DRF test client  
- `user_factory`: for creating users  
- `company_factory`: for creating companies

## Tech Stack

- Python 3.12  
- Django 5.2  
- Django REST Framework  
- PostgreSQL  
- Docker  
- Poetry  
- Pytest  
- drf-spectacular  
- Jazzmin