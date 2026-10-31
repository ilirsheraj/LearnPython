from functools import cached_property

class Client:
    def __init__(self):
        print("Setting up the client ...")

    def query(self, **kwargs):
        print(f"Performing a query {kwargs}")

class CachedPropertyManager:
    @cached_property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

def main():
    manager = CachedPropertyManager()
    manager.perform_query(object_id=42)
    manager.perform_query(name_ilike="%Pyhton")
    del manager.client
    manager.perform_query(age_gte=18)

if __name__ == "__main__":
    main()