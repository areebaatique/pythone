from resource_interface import Resource

class FileResource:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.file = None

    def connect(self):
        self.file = open(self.filepath, 'r+')
        print(f"File {self.filepath} opened.")

    def close(self):
        if self.file:
            self.file.close()
            print(f"File {self.filepath} closed.")

    def read(self, query: str) -> str:
        # For simplicity, ignore 'query'
        self.file.seek(0)
        return self.file.read()

    def write(self, data: str) -> None:
        self.file.write(data)
        self.file.flush()
