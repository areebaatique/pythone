from abc import ABC, abstractmethod

class DataStore(ABC):
    @abstractmethod
    def store(self, key: str, value: str) -> bool:
        pass

    @abstractmethod
    def retrieve(self, key: str) -> str | None:
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        pass

    @abstractmethod
    def list_keys(self) -> list[str]:
        pass

class MemoryStore(DataStore):
    def __init__(self):
        self.storage = {}

    def store(self, key: str, value: str) -> bool:
        self.storage[key] = value
        return True

    def retrieve(self, key: str) -> str | None:
        return self.storage.get(key)

    def delete(self, key: str) -> bool:
        return self.storage.pop(key, None) is not None

    def list_keys(self) -> list[str]:
        return list(self.storage.keys())

# --- Test Code ---
if __name__ == "__main__":
    store = MemoryStore()
    store.store("name", "Areeba")
    print("Retrieve:", store.retrieve("name"))
    print("All Keys:", store.list_keys())
    store.delete("name")
    print("After Delete:", store.retrieve("name"))
