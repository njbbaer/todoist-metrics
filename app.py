from todoist_metrics import TodoistMetrics
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    pressure_score = TodoistMetrics().calculate_pressure_score()
    return render_template('home.html', pressure_score=pressure_score)