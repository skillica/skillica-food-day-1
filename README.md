# Skillica Food — Day 1

A simple Django starter project for Skillica students.

This README shows how to **clone the repo** and **run the project locally** step-by-step.

---

## Prerequisites

- Python 3.12+ installed (3.12 or 3.13+ recommended)
- Git installed
- (Optional) MySQL / PostgreSQL if the project is configured to use them — default settings typically use SQLite.

---

## 1. Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/skillica/skillica-food-day-1.git
cd skillica-food-day-1
```

---

## 2. Create and activate a virtual environment

Windows (Command Prompt)

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation you should see (.venv) in your prompt.

---

## 3. Upgrade pip and install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the repository does not include requirements.txt, install Django and other packages manually, for example:

```bash
pip install django
```

---

## 4. Database migrations

Run migrations to create database tables:

```bash
python manage.py migrate
```

If you need an initial admin user:

```bash
python manage.py createsuperuser
# follow the prompts to create username, email and password
```

---

## 5. Collect static files (if needed)

For development this is usually not required, but if static files are configured to be collected:

```bash
python manage.py collectstatic --noinput
```

---

## 6. Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser at: http://127.0.0.1:8000/

---

## 7. Common commands

- Run shell: python manage.py shell
- Run tests (if provided): python manage.py test
- Make new migration files: python manage.py makemigration
- Show available URLs: python manage.py show_urls (Django extensions)

## Troubleshooting & tips

- “Requested setting DEBUG, but settings are not configured” — this happens when you run django-admin runserver without telling Django which settings to use. Use python manage.py runserver (recommended) or set DJANGO_SETTINGS_MODULE before using django-admin.
- Templates / form rendering issues — if you see Invalid block tag 'form.as_p', make sure you use {{ form.as_p }} (double curly braces) — form.as_p is not a template tag.

- eval() warnings — if the project reads serialized Python data using eval(), be careful. Prefer safer options like ast.literal_eval() or JSON for reading data files.

- Database driver errors — if the project uses MySQL/Postgres, install the driver:

- MySQL: pip install mysqlclient (may require OS libraries)

- Postgres: pip install psycopg2-binary

- Permission / port in use — if port 8000 is busy: python manage.py runserver 0.0.0.0:8001 (or any free port)

## Licensing

This repository is provided under the custom MIT-style educational license (see LICENSE file).
You may use and modify the code for educational / non-commercial purposes.

## Need help?

If something fails, copy the terminal error and share it in the class chat or open an issue in the repository.
I can help debug common errors quickly.
