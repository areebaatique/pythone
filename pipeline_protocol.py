from typing import Protocol, Any, runtime_checkable


# Protocols

@runtime_checkable
class FileReader(Protocol):
    def read(self, filepath: str) -> Any:
        ...


@runtime_checkable
class FileWriter(Protocol):
    def write(self, data: Any, filepath: str) -> None:
        ...


@runtime_checkable
class FileProcessor(Protocol):
    def process(self, data: Any) -> Any:
        ...


# Concrete Readers

import csv
import json


class CSVReader:
    def read(self, filepath: str) -> list[dict]:
        with open(filepath, newline='') as f:
            return list(csv.DictReader(f))


class JSONReader:
    def read(self, filepath: str) -> Any:
        with open(filepath) as f:
            return json.load(f)


class TextReader:
    def read(self, filepath: str) -> str:
        with open(filepath) as f:
            return f.read()


# Concrete Writers

class CSVWriter:
    def write(self, data: list[dict], filepath: str) -> None:
        if not data:
            return
        with open(filepath, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class JSONWriter:
    def write(self, data: Any, filepath: str) -> None:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)


class TextWriter:
    def write(self, data: str, filepath: str) -> None:
        with open(filepath, "w") as f:
            f.write(data)


# Concrete Processors

class CSVValidator:
    def process(self, data: list[dict]) -> list[dict]:
        # Just an example: remove rows missing any field
        return [row for row in data if all(value.strip() != "" for value in row.values())]


class CSVTransformer:
    def process(self, data: list[dict]) -> list[dict]:
        # Example: uppercase all values
        return [{k: v.upper() if isinstance(v, str) else v for k, v in row.items()} for row in data]
from typing import Protocol, Any, runtime_checkable


# Protocols

@runtime_checkable
class FileReader(Protocol):
    def read(self, filepath: str) -> Any:
        ...


@runtime_checkable
class FileWriter(Protocol):
    def write(self, data: Any, filepath: str) -> None:
        ...


@runtime_checkable
class FileProcessor(Protocol):
    def process(self, data: Any) -> Any:
        ...


# Concrete Readers

import csv
import json


class CSVReader:
    def read(self, filepath: str) -> list[dict]:
        with open(filepath, newline='') as f:
            return list(csv.DictReader(f))


class JSONReader:
    def read(self, filepath: str) -> Any:
        with open(filepath) as f:
            return json.load(f)


class TextReader:
    def read(self, filepath: str) -> str:
        with open(filepath) as f:
            return f.read()


# Concrete Writers

class CSVWriter:
    def write(self, data: list[dict], filepath: str) -> None:
        if not data:
            return
        with open(filepath, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


class JSONWriter:
    def write(self, data: Any, filepath: str) -> None:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)


class TextWriter:
    def write(self, data: str, filepath: str) -> None:
        with open(filepath, "w") as f:
            f.write(data)


# Concrete Processors

class CSVValidator:
    def process(self, data: list[dict]) -> list[dict]:
        # Just an example: remove rows missing any field
        return [row for row in data if all(value.strip() != "" for value in row.values())]


class CSVTransformer:
    def process(self, data: list[dict]) -> list[dict]:
        # Example: uppercase all values
        return [{k: v.upper() if isinstance(v, str) else v for k, v in row.items()} for row in data]


class JSONKeyFilter:
    def __init__(self, keys: set[str]):
        self.keys = keys

    def process(self, data: dict) -> dict:
        return {k: v for k, v in data.items() if k in self.keys}


class TextUppercaser:
    def process(self, data: str) -> str:
        return data.upper()


# Processing Pipeline

class ProcessingPipeline:
    def __init__(self, reader: FileReader, processor: FileProcessor, writer: FileWriter):
        self.reader = reader
        self.processor = processor
        self.writer = writer

    def run(self, input_path: str, output_path: str) -> None:
        data = self.reader.read(input_path)
        processed_data = self.processor.process(data)
        self.writer.write(processed_data, output_path)


# Example usage

if __name__ == "__main__":
    pipeline = ProcessingPipeline(
        reader=CSVReader(),
        processor=CSVTransformer(),
        writer=CSVWriter(),
    )
    pipeline.run("input.csv", "output.csv")
