# Trao Exchange Platform

A platform for exchanging items built with Flask and PostgreSQL.

## Local Development

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and configure your environment variables:
```bash
cp .env.example .env
```

4. Run the development server:
```bash
flask run
```

## Deployment on Render.com

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn -c gunicorn.conf.py "exchange_items:create_app()"`
   - Python Version: 3.10.0

4. Add the following environment variables:
   - `FLASK_APP`: exchange_items
   - `FLASK_ENV`: production
   - `DB_USERNAME`: Your database username
   - `DB_PASSWORD`: Your database password
   - `DB_HOST`: Your database host
   - `DB_NAME`: Your database name

5. Deploy!