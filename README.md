# Attendance Management (sdpp)

Simple Django app to manage students and attendance.

**Prerequisites**
- Python 3.11+ and virtualenv
- Windows PowerShell (commands shown below)

**Setup**
1. Create and activate a virtual environment (if not present):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Install dependencies (if you have a `requirements.txt`):
```powershell
pip install -r requirements.txt
# or at minimum:
pip install Django
```
3. Apply migrations:
```powershell
python manage.py migrate
```
4. (Optional) Create a superuser:
```powershell
python manage.py createsuperuser
```

**Run development server**
```powershell
python manage.py runserver
```
Open http://127.0.0.1:8000/attendance/mark/ to mark attendance.

**Tests**
Run app tests:
```powershell
python manage.py test attendance
```

**Notes & Troubleshooting**
- If templates were edited and you see template errors, restart the dev server to clear the cached templates.
- If the Django test client reports `Invalid HTTP_HOST header: 'testserver'`, add `'testserver'` to `ALLOWED_HOSTS` in `attendence_site/settings.py` during testing or set `settings.ALLOWED_HOSTS` at runtime.
- The `mark attendance` page URL: `/attendance/mark/` — check that `{% csrf_token %}` is present in the form and that the server logs show POST handling.

If you want, I can also add a `requirements.txt`, or commit the README for you.