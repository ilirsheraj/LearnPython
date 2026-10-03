def connect(**options):
    """
    Write a function to connect to a database.
    It can connect to a default database without any parameters
    (thus default), or it can connect to any other database with
    parameters defined by the user
    """

    conn_params = {
            "host": options.get("host", "127.0.0.1"),
            "port": options.get("port", 5432),
            "user": options.get("user", ""),
            "pwd": options.get("pwd", ""),
            }

    print(conn_params)

def main():
    print("Pass the function without parameters")
    connect()
    print()
    host='127.0.0.42'
    port=5433
    print(f"Pass the function with host: {host} and port: {port}")
    connect(host = "127.0.0.42", port = 5433)
    print()
    connect(port=5431, user="fab", pwd="gandalf")

if __name__ == "__main__":
    main()

