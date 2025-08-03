# URL Shortener Service

A minimal Flask-based URL shortener service similar to Bit.ly or TinyURL.

## 🔧 Features
- POST `/api/shorten`
- GET `/<short_code>`
- GET `/api/stats/<short_code>`

## 🧪 Tech Stack
- Python 3.8+
- Flask
- Pytest
- In-memory dictionary

## 🚀 Getting Started
```
pip install -r requirements.txt
python -m flask --app app.main run
```

## ✅ Example
```
curl -X POST http://localhost:5000/api/shorten -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}'
```

## 🧪 Run Tests
```
pytest
```
