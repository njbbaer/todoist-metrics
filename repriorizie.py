import todoist
import os

api = todoist.TodoistAPI(os.getenv('TODOIST_API_KEY'))
tasks = api.state['items']

def find_movable(tasks, )