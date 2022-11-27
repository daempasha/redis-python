import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept()  # wait for client
    connection.recv(1024)
    connection.send("+PONG\r\n")


if __name__ == "__main__":
    main()
