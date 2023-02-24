import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', 8787))
    socket_server.listen()

    selector.register(fileobj=socket_server, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(socket_server: socket.socket):
    socket_client, addr = socket_server.accept()
    print(f'Connection from {addr}')

    selector.register(fileobj=socket_client, events=selectors.EVENT_READ, data=send_message)


def send_message(socket_client: socket.socket):
    request = socket_client.recv(2048)
    if request:
        response = 'Hello, world!\n'.encode()
        socket_client.send(response)
    else:
        selector.unregister(fileobj=socket_client)
        socket_client.close()


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
