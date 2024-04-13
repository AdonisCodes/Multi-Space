import socket
import time

# Type of the current game instance
game_client_type = input("What type are you? (h/j): ")
print("X", [1, 5])


def server():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 12357))
    sock.listen()
    connection, address = sock.accept()
    print("Connection made by", address[0])

    return connection


def client():
    sock = socket.socket()
    sock.connect(("127.0.0.1", 12357))
    sock.sendall(b"Hello, world!")
    data = sock.recv(1024)
    print(data)

    return sock


def gameloop(connection):
    with connection:
        while True:
            data = connection.recv(1024)
            if data:
                print("Data", data)
            else:
                print("No data")

            connection.sendall(data)


if game_client_type == "h":
    # TODO: Launch the server waiter
    server()
else:
    # TODO: Connect to the server
    connection = client()
    while True:
        connection.sendall(input("Send To Server").encode())
