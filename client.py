import socket

# Type of the current game instance
game_client_type = input("What type are you? (h/j): ")
print("X", [1, 5])


def server(): ...
def client(): ...


def gameloop(connection): ...


if game_client_type == "h":
    # TODO: Launch the server waiter
    connection = server()
    gameloop(connection)
else:
    # TODO: Connect to the server
    connection = client()
    gameloop(connection)
