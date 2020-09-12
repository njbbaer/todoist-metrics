import todoist
import dateutil.parser
from datetime import datetime
from dotenv import load_dotenv
import os

class TodoistMetrics:
  def __init__(self):
    self.api = todoist.TodoistAPI(os.getenv('TODOIST_API_KEY'))
    self.api.sync()

  def count_items(self, priority):
    return sum(item['priority'] == priority for item in self._active_items())
  
  def _items(self):
    return self.api.state['items']

  def _active_items(self):
    def is_active(item):
      return not item['due'] or dateutil.parser.isoparse(item['due']['date']) < datetime.today()

    return list(filter(is_active, self._items()))
