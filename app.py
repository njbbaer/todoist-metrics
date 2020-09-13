from todoist_metrics import TodoistMetrics
from flask import Flask, render_template, request, Response
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    todoist = TodoistMetrics()
    return render_template('home.html', 
        first_priority  = todoist.count_items(priority=4),
        second_priority = todoist.count_items(priority=3),
        third_priority  = todoist.count_items(priority=2)
    )

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json)
    return Response(status=200)