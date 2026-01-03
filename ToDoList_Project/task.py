class Task:
    def __init__(self,id,title,description,status="Incomplete"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
    
    def mark_complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            status=data['status']
        )
    

