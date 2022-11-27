import socket


def main():
    server_socket = socket.create_server(("localhost", 6379))
    connection, address = server_socket.accept()  # wait for client

    while True:
        connection.recv(1024)
        connection.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
