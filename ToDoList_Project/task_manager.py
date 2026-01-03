import json
from task import Task 

class TaskManager:
    def __init__(self,storage="tasks.json"):
        self.storage = storage
        self.tasks = []

    def add_task(self,title,description):
        new_id= len (self.tasks) + 1
        task = Task(new_id,title,description,"incomplete")
        self.tasks.append(task)
        self._save()


    def view_tasks(self):
        return self.tasks


    def complete_task(self,task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self._save()
                return True
        return False
    
    
    def delete_task(self,task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self._save()
                return True
        return False


    def _save(self):
        data = [t.to_dict() for t in self.tasks]
        with open(self.storage, "w") as f:
            json.dump(data, f, indent=2)


