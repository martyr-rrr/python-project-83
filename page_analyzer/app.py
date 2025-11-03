import os
from flask import Flask, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    # Пока просто возвращаем заглушку
    return f"Анализ URL: {url} - функция в разработке"
