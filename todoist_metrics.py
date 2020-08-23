import todoist
import dateutil.parser
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

class TodoistMetrics:
  PRESSURE_SCORE_TABLE = { 1: 0, 2: 1, 3: 4, 4: 16 }

  def __init__(self):
    self.api = todoist.TodoistAPI(os.getenv("TODOIST_API_KEY"))
    self.api.sync()

  def calculate_pressure_score(self):
    pressure_score = 0
    for item in self._active_items():
      pressure_score += self.PRESSURE_SCORE_TABLE[item['priority']]
    return pressure_score
  
  def _items(self):
    return self.api.state['items']

  def _active_items(self):
    def is_active(item):
      return not item['due'] or dateutil.parser.isoparse(item['due']['date']) < datetime.today()

    return list(filter(is_active, self._items()))


if __name__ == '__main__':
  tm = TodoistMetrics()
  print(tm.calculate_pressure_score())
