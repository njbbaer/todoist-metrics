import todoist
import dateutil.parser
from datetime import datetime
from dotenv import load_dotenv
import os


class TodoistMetrics:
    def __init__(self):
        self.api = todoist.TodoistAPI(os.getenv('TODOIST_API_KEY'))
        self.api.sync()
        tasks = self.api.state['items']
        self.tasks = [Task(task) for task in tasks]

    def count_active_tasks(self, priority):
        return len(self.get_tasks(priority))

    def get_oldest_tasks(self):
        def oldest_sort_key(task):
            return task.due_date() or task.date_added()

        return sorted(self.get_tasks(3), key=oldest_sort_key)

    def get_tasks(self, priority):
        def in_criteria(task):
            return task.has_priority(priority) and task.is_active()

        return list(filter(in_criteria, self.tasks))


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
        due = self.task['due']
        if not due: return None
        return dateutil.parser.isoparse(due['date'])

    def date_added(self):
        dt = dateutil.parser.isoparse(self.task['date_added'])
        return dt.replace(tzinfo=None)
