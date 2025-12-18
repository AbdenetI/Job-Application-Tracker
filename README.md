# Job Application Tracker

A full-stack Django web application designed to streamline the job search process by helping users organize and track their job applications, companies, and follow-ups in one centralized platform.

## Overview

Job hunting can be overwhelming when managing dozens of applications across multiple companies. This application solves that problem by providing an intuitive interface to track application statuses, store company information, manage job postings, and visualize your job search progress through an interactive dashboard.

## Tech Stack

**Backend:**
- Python 3.13
- Django 5.x
- SQLite (development database)
- Django Signals for automated tracking

**Frontend:**
- Bootstrap 5 (responsive design)
- Django Templates (server-side rendering)
- HTML5/CSS3

**Key Libraries:**
- django-filter - Advanced filtering and search
- WhiteNoise - Static file serving for production

## Features

### Authentication & Authorization
- Secure user registration and login system
- Password-protected user sessions
- Per-user data isolation

### Company Management
- Create and manage company profiles
- Store company details and contact information
- Track applications per company

### Job Posting Tracking
- Add job postings with detailed information
- Link jobs to specific companies
- Maintain job descriptions and requirements

### Application Management
- Track application status (Applied, Interview, Offer, Rejected, etc.)
- Record application dates and deadlines
- Add notes and follow-up reminders
- Automatic status change timeline using Django signals

### Dashboard & Analytics
- Visual overview of application statistics
- Quick access to pending follow-ups
- Filter applications by status, company, or keywords
- Search functionality across all applications

### Advanced Filtering
- Multi-criteria filtering powered by django-filter
- Real-time search across companies and positions
- Status-based filtering for workflow management

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/AbdenetI/Job-Application-Tracker.git
cd Job-Application-Tracker
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py migrate
```

5. **Create admin user**
```bash
python manage.py createsuperuser
```

6. **Start development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Application: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

### Optional: Load Demo Data
```bash
python manage.py seed_demo
# Login credentials: demo / demo1234
```

## Project Structure

```
Job-Application-Tracker/
├── jobtracker/           # Main project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI application entry
├── tracker/              # Core application module
│   ├── models.py         # Database models (Company, Job, Application)
│   ├── views.py          # View logic and controllers
│   ├── forms.py          # Django forms for data input
│   ├── filters.py        # django-filter configurations
│   ├── signals.py        # Automated tracking logic
│   ├── urls.py           # App-specific URL routing
│   └── migrations/       # Database migration files
├── templates/            # HTML templates
│   ├── base.html         # Base template with Bootstrap
│   ├── auth/             # Authentication templates
│   └── tracker/          # Application templates
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Key Models

- **Company**: Stores company information and contact details
- **Job**: Represents job postings linked to companies
- **Application**: Tracks individual job applications with status timeline

## Configuration Notes

- Default timezone: America/Chicago (configurable in settings.py)
- Static files served via WhiteNoise (production-ready)
- Bootstrap 5 loaded via CDN for responsive UI
- SQLite for development (easily switchable to PostgreSQL/MySQL for production)

## Future Enhancements

- Email notifications for follow-up reminders
- Calendar integration for interview scheduling
- Export functionality (PDF/Excel reports)
- Analytics dashboard with charts and visualizations
- Resume and cover letter attachment management
- API endpoints for mobile app integration
- Multi-user collaboration features
- Integration with job boards (LinkedIn, Indeed, etc.)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Django Shell
```bash
python manage.py shell
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Contact

Created by Abdenet - [GitHub Profile](https://github.com/AbdenetI)
