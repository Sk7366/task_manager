class Task:

    def __init__(
        self,
        title,
        description,
        priority,
        due_date,
        status="pending"
    ):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status