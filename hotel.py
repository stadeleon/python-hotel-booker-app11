class Hotel:
    def __init__(self, data: dict):
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.capacity = data['capacity']
        self.available = data['available'].lower() == 'yes'

    def book(self):
        self.available = False

    def is_available(self) -> bool:
        return self.available

    def __str__(self):
        return f"{self.id},{self.name},{self.city},{self.capacity}," \
               f"{'yes' if self.available else 'no'}"
