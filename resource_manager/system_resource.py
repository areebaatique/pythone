import subprocess
from resource_interface import Resource

class SystemCommandResource:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("System command resource ready")

    def close(self):
        self.connected = False
        print("System command resource closed")

    def read(self, query: str) -> str:
        # Execute the command and return output
        result = subprocess.run(query, shell=True, capture_output=True, text=True)
        return result.stdout.strip()

    def write(self, data: str) -> None:
        # Not applicable for system commands, but simulate warning
        print(f"Write operation not supported for system commands")
