# GYM
Using Django



### Gym Management System
This is a Django-based Gym Management System that allows staff to manage gym-related data such as enquiries, equipment, plans, and members. The system includes basic authentication for staff and provides functionalities to add, view, and delete records.

## Table of Contents
- Features
- Installation
- Usage
- Project Structure
- Screenshots
- Contributing
- License


## Features
- Authentication: Secure login system for staff members.
- Enquiries: Add, view, and delete enquiries.
- Equipment: Manage gym equipment details.
- Plans: Manage membership plans.
- Members: Add, view, and delete gym members.


## Installation
# Prerequisites
- Python 3.x
- Django 3.x or later
- Virtualenv (optional but recommended)

# Steps
1. Clone the repository:

```
git clone https://github.com/Ainy07/GYM.git
cd GYM
``` 
2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Create a superuser:


```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

7. Access the application:
Open your browser and go to http://127.0.0.1:8000/.

## Usage
1. Home: Access the admin panel or view available data.
2. Add Records: Use the navigation bar to add enquiries, equipment, plans, and members.
3. View Records: Access the list views to see all records and manage them.
4. Delete Records: Use the delete buttons in the list views to remove records.


## Project Structure
- gym_management/: Django project settings.
- app_name/: Main application containing models, views, and templates.
- templates/: HTML templates for the web pages.
- static/: Static files (CSS, JavaScript, images).
- requirements.txt: List of dependencies.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.