type DatabasePort = int

def connect_to_database(host: str, port: DatabasePort):
    print(f"Connecting to {host} on port {port}")

def main():
    host = "localhost"
    port = "5432"
    connect_to_database(host, port)

if __name__ == '__main__':
    main()