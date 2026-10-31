class Client:
    def __init__(self):
        print("Setting up the client ...")

    def query(self, **kwargs):
        print(f"Performing a query {kwargs}")

class Manager:
    @property
    def client(self):
        if not hasattr(self, "_client"):
            self._client = Client()
        return self._client

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

def main():
    clnt = Client()
    print(clnt.query())
    mng = Manager()
    print(mng.perform_query())

if __name__ == "__main__":
    main()