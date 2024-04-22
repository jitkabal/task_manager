#task manager
from datetime import datetime as datetime

class Task:
    def __init__ (self, description: str)->None:
        self.description = description
        self.timestamp = datetime.now()

aktualni_klic = 0
databaze_tasku = {}

databaze_tasku[aktualni_klic] = Task(...)
aktualni_klic += 1

    def __str__(self):
        return f"{self.timestamp} + {self.description}"    
    
ukol = Task("Prvni Ukol", timestamp=any)  
print(ukol)





