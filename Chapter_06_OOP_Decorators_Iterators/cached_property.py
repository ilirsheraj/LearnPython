class Client:
    def __init__(self):
        print("Setting up the client ...")

    def query(self, **kwargs):
        print(f"Performing a query {kwargs}")

class Manager:
    @property
    def client(self):
        return Client()

    def perform_query(self, **kwargs):
        return self.client.query(**kwargs)

def main():
    clnt = Client()
    print(clnt.query())
    mng = Manager()
    print(mng.perform_query())

if __name__ == "__main__":
    main()