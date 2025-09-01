# Recipe Management API

A clean Django + DRF backend where users can register/login and manage cooking recipes.
Includes JWT auth, filtering by category and ingredients, and OpenAPI docs.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Create project files
django-admin startproject --version  # should print 5.x

# ENV
cp .env.example .env    # or copy manually on Windows
# (optional) edit .env to set SECRET_KEY, ALLOWED_HOSTS...

# Run initial setup
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Home page: http://127.0.0.1:8000/
- API docs (Swagger UI): http://127.0.0.1:8000/api/docs/
- OpenAPI JSON: http://127.0.0.1:8000/api/schema/

## Auth (JWT)
- `POST /register/` → create user
- `POST /login/` → obtain JWT tokens `{access, refresh}`
- `POST /token/refresh/` → refresh access

Include the **access** token in requests: `Authorization: Bearer <token>`.

## Recipes
- `GET /recipes/` → list (supports `?ingredient=egg` and `?category=dessert`)
- `POST /recipes/` → create (auth required)
- `PUT /recipes/<id>/` → update (owner only)
- `DELETE /recipes/<id>/` → delete (owner only)

## Deploy on PythonAnywhere (high level)
1. Upload the project folder or clone from GitHub.
2. Create a virtualenv and install `requirements.txt`.
3. In **Web** tab, set WSGI app to point to `recipe_manager.wsgi:application`.
4. Add env vars in **Web → Environment Variables** (or load `.env` via WSGI file).
5. Set static (if needed): `/static/` → `<project>/staticfiles` then `python manage.py collectstatic`.
6. Reload web app.

## Tests (example)
Run: `pytest` (or `python manage.py test`) — sample tests are included under each app.

## Project layout
```
recipe_management_api/
  manage.py
  recipe_manager/
  users/
  recipes/
  templates/
  static/
```


## Web dashboard (session auth)
A simple Bootstrap UI is included:
- **Register**: `/accounts/register/`
- **Login**: `/accounts/login/`
- **Dashboard**: `/dashboard/` (requires login)
  - Create: `/recipes/new/`
  - Edit: `/recipes/<id>/edit/`
  - Delete: `/recipes/<id>/delete/`

This UI uses Django's session authentication (separate from JWT). You can use both: UI for humans, JWT API for programmatic access.
