# JobTracker (Django MVP)

A server-rendered Django app to track job applications.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Optional demo data:
```bash
python manage.py seed_demo
# Login with: demo / demo1234
```

## Features
- Auth (register/login/logout)
- Create Companies, Jobs, Applications
- Filters (status, company, search) via django-filter
- Dashboard with counts + follow-ups
- Status change timeline (signals)
- SQLite (dev) + Whitenoise for static files (prod-ready)

## Notes
- Timezone set to America/Chicago.
- Bootstrap 5 loaded via CDN in templates/base.html.
