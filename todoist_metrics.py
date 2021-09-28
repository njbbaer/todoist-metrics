import todoist
import dateutil.parser
from datetime import datetime
from dotenv import load_dotenv
import os

class TodoistMetrics:
  def __init__(self):
    self.api = todoist.TodoistAPI(os.getenv('TODOIST_API_KEY'))
    self.api.sync()

  def tasks(self):
    tasks = self.api.state['items']
    return [Task(task) for task in tasks]

  def count_active_tasks(self, priority):
    def in_criteria(task):
      return task.has_priority(priority) and task.is_active()
    
    filtered_tasks = list(filter(in_criteria, self.tasks()))
    return len(filtered_tasks)

class Task:
  def __init__(self, task):
    self.task = task

  def has_priority(self, priority):
    return self.task['priority'] == priority

  def is_active(self):
    return self.task['checked'] == 0 and (
        not self.task['due'] 
        or self.due_date() < datetime.today()
      )

  def due_date(self):
    return dateutil.parser.isoparse(self.task['due']['date'])