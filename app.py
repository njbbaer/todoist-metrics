from todoist_metrics import TodoistMetrics
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    tm = TodoistMetrics()
    return render_template('home.html', 
        first_priority  = tm.count_active_items(priority=4),
        second_priority = tm.count_active_items(priority=3),
        third_priority  = tm.count_active_items(priority=2),
        fourth_priority = tm.count_active_items(priority=1),
    )

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json)
    return Response(status=200)