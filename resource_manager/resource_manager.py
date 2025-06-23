from typing import List
from resource_interface import Resource

class ResourceManager:
    def __init__(self):
        self.resources: List[Resource] = []

    def add_resource(self, resource: Resource):
        self.resources.append(resource)

    def connect_all(self):
        for r in self.resources:
            r.connect()

    def close_all(self):
        for r in self.resources:
            r.close()

    def read_all(self, query: str):
        results = {}
        for r in self.resources:
            try:
                results[type(r).__name__] = r.read(query)
            except Exception as e:
                results[type(r).__name__] = f"Error reading: {e}"
        return results

    def write_all(self, data: str):
        for r in self.resources:
            try:
                r.write(data)
            except Exception as e:
                print(f"Error writing to {type(r).__name__}: {e}")

    def __enter__(self):
        self.connect_all()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_all()
