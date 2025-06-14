# 🔗 URL Shortener Web Application

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A full-featured URL shortening service built with Python and Flask, featuring a modern web interface and REST API.

## ✨ Features

- **Instant URL shortening** with 6-character codes
- **Reliable redirects** with proper HTTP status codes
- **Duplicate URL detection** - Same URL = Same short code
- **Mobile-friendly** responsive web interface
- **REST API** for programmatic access
- **Docker-ready** for easy deployment
- **SQLite/PostgreSQL** database support

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- (Optional) Docker for containerized deployment

### Local Installation
```bash
# Clone the repository
git clone https://github.com/Prasunnandi/URL_Shortner.git
cd URL_Shortner


# Install dependencies
pip install -r backend/requirements.txt

# Initialize database and run server
python backend/app.py
Access the web interface at: http://localhost:5000
```
Docker Deployment

```bash
docker-compose up -d
Access: http://localhost:5000
```

📚 API Documentation
Shorten URL
Endpoint: POST /api/shorten
Request:
```
json
{
  "url": "https://example.com/very/long/url"
}
Response:

json
{
  "original_url": "https://example.com/very/long/url",
  "short_url": "http://yourdomain/AbCdEf"
}
Redirect
Endpoint: GET /{short_code}
Response: 301 Redirect to original URL
```
🏗 Project Structure
```
text
URL_Shortner/
├── backend/
│   ├── app.py         # Flask application
│   ├── models.py      # Database models
│   ├── requirements.txt
│   └── tests/         # Unit tests
├── frontend/
│   ├── static/        # CSS/JS assets
│   └── templates/     # HTML templates
├── docker-compose.yml # Container config
└── README.md         # This file
```
🛠 Development
Set up virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Install dev requirements:

```bash
pip install -r backend/requirements.txt
```
Run with debug mode:

```bash
FLASK_DEBUG=1 python backend/app.py
```
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
PrasunNandi - www.linkedin.com/in/prasun-nandi-07b9841a9

ProjectLink: https://github.com/Prasunnandi/URL_Shortner

1. Copy this entire content
2. Create a new `README.md` file in your project root
3. Paste and save
4. Customize the contact details and URLs
5. Commit to GitHub
