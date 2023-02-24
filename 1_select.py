import socket
from select import select

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind(('localhost', 8787))
socket_server.listen()

to_monitor = []


def accept_connection(socket_server: socket.socket):
    socket_client, addr = socket_server.accept()
    print(f'Connection from {addr}')
    to_monitor.append(socket_client)


def send_message(socket_client: socket.socket):
    request = socket_client.recv(2048)
    if request:
        response = 'Hello, world!\n'.encode()
        socket_client.send(response)
    else:
        socket_client.close()
        to_monitor.remove(socket_client)


def event_loop():
    ready_to_read, _, _ = select(to_monitor, [], [])

    for sock in ready_to_read:
        if sock is socket_server:
            accept_connection(sock)
        else:
            send_message(sock)


if __name__ == '__main__':
    to_monitor.append(socket_server)
    while True:
        event_loop()
