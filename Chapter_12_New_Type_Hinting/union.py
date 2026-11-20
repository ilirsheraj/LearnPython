from typing import Union

def connect_to_database(host: str, port: Union[int, str]):
    print(f"Connecting to {host} on port {port}...")

def connect_to_db(host: str, port: int|str):
    print(f"Connecting to {host} on port {port}...")

def main():
    host = "localhost"
    port = "5432"
    connect_to_database(host, port)
    connect_to_db(host, port)

if __name__ == "__main__":
    main()
