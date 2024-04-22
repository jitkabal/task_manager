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

def add_task(description:str)-> None:
    task = Task(description)
    databaze_tasku[aktualni_klic] = task
    aktualni_klic += 1

def remove_task(task_id:int) -> None:
    if task_id in databaze_tasku:
        databaze_tasku.pop(task_id)    

def 
    def __str__(self):
        return f"{self.timestamp} + {self.description}"    
    
ukol = Task("Prvni Ukol", timestamp=any)  
print(ukol)





