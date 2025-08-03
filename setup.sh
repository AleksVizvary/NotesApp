#!/bin/bash

echo "🔧 Creating venv..."
python3 -m venv venv

echo "🚀 Activating venv..."
source venv/bin/activate


echo "📦 Installing requirements..."
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "⚠️ No requirements.txt – installing django."
    pip install django
fi

echo "🛠️ DB migrations..."
python manage.py makemigrations
python manage.py migrate

echo "✅ Running server..."
python manage.py runserver
