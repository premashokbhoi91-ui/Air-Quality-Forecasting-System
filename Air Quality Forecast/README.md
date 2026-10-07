# Air Quality Forecast

**Install:** `pip install -r requirements.txt`
**Run:** `python app.py`
**Browser:** http://127.0.0.1:5000

**Database:** `database/air_quality.db` (SQLite, created automatically on first run; table `users`: id, name, email, password_hash, created_at)

**Registration:** `/register` form -> Flask validates (required fields, matching passwords, unique email) -> password hashed with Werkzeug -> saved in `users` -> you are logged in and sent to the dashboard.

**Public home:** `/` (dashboard) opens without login and shows Login / Register buttons.

**Login:** `/login` form -> Flask looks up the email in `users` -> `check_password_hash()` -> on success a Flask session is created and you land on the dashboard (`/`). Once logged in, click the avatar (first letter of your name) -> My Profile (`/profile`) or Logout. `/logout` clears the session and returns to the public dashboard. Forecast, Locations, Reports, Settings and Profile require login.

**DB Browser for SQLite:** File -> Open Database -> select `database/air_quality.db` -> Browse Data tab -> table `users`.
