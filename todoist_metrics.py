import todoist
import dateutil.parser
from datetime import datetime
from dotenv import load_dotenv
import os

class Item:
  def __init__(self, item):
    self.item = item

  def has_priority(self, priority):
    return self.item['priority'] == priority

  def is_active(self):
    return self.item['checked'] == 0 and (
        not self.item['due'] 
        or dateutil.parser.isoparse(self.item['due']['date']) < datetime.today()
      )

class Todoist:
  def __init__(self):
    self.api = todoist.TodoistAPI(os.getenv('TODOIST_API_KEY'))
    self.api.sync()

  def items(self):
    items = self.api.state['items']
    return [Item(item) for item in items]

  def count_active(self, priority):
    def in_criteria(item):
      return item.has_priority(priority) and item.is_active()
    
    filtered_items = list(filter(in_criteria, self.items()))
    return len(filtered_items)