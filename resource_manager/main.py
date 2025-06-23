from resource_manager import ResourceManager
from file_resource import FileResource
from api_resource import APIResource
from db_resource import DBResource
from system_resource import SystemCommandResource

def main():
    file_res = FileResource("test.txt")
    api_res = APIResource("https://api.example.com/data")
    db_res = DBResource(":memory:")  # in-memory SQLite DB
    sys_res = SystemCommandResource()

    manager = ResourceManager()
    manager.add_resource(file_res)
    manager.add_resource(api_res)
    manager.add_resource(db_res)
    manager.add_resource(sys_res)

    with manager:
        print("Reading from all resources:")
        results = manager.read_all("SELECT sqlite_version();")  # example query
        for res_name, output in results.items():
            print(f"{res_name}: {output}")

        print("\nWriting sample data to all resources:")
        manager.write_all("""
        CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT);
        INSERT INTO test (name) VALUES ('Alice');
        """)

        print("\nRunning system command read:")
        cmd_output = sys_res.read("echo Hello World")
        print(f"SystemCommandResource output: {cmd_output}")

if __name__ == "__main__":
    main()
