from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
