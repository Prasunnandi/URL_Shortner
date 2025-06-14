# URL Shortener

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-red)

A self-hosted URL shortener service with analytics.

## Features
- Generates short codes (6 characters)
- Tracks click counts
- Simple web interface
- SQLite database

## Setup
```bash
# 1. Install dependencies
pip install -r backend/requirements.txt

# 2. Initialize database
python backend/models.py

# 3. Run the server
python backend/app.py