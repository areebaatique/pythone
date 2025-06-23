from resource_interface import Resource

class APIResource:
    def __init__(self, url: str):
        self.url = url
        self.connected = False

    def connect(self):
        # Simulate connection
        self.connected = True
        print(f"Connected to API at {self.url}")

    def close(self):
        self.connected = False
        print(f"Disconnected from API at {self.url}")

    def read(self, query: str) -> str:
        # Simulate GET request response
        return f"Data fetched from {self.url} with query '{query}'"

    def write(self, data: str) -> None:
        # Simulate POST request
        print(f"Data '{data}' sent to {self.url}")
