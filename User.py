class User:
    def __init__(self, user_id: int, name: str):
        self.id = user_id
        self.name = name

    def get_name(self):
        return self.name
