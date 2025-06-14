from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random
import os

# Initialize Flask app with custom template and static folders
app = Flask(__name__, 
            template_folder='../frontend/templates',
            static_folder='../frontend/static')

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    original_url = data['url']
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url
    
    existing_url = Url.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({
            'original_url': original_url,
            'short_url': f"{request.host_url}{existing_url.short_code}"
        })
    
    short_code = generate_short_code()
    while Url.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code()
    
    new_url = Url(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify({
        'original_url': original_url,
        'short_url': f"{request.host_url}{short_code}"
    })

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = Url.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)