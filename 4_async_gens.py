import socket
from select import select

to_read = {}
to_write = {}

tasks = []


def server():
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_server.bind(('localhost', 8787))
    socket_server.listen()

    while True:
        yield 'read', socket_server
        client_socket, addr = socket_server.accept()
        print(f'Connection from {addr}')

        tasks.append(client(client_socket, addr))


def client(client_socket, addr):
    while True:
        yield 'read', client_socket

        message = client_socket.recv(4096)
        if not message:
            break
        else:
            yield 'write', client_socket
            client_socket.send(f'Hello, user from {addr} \n'.encode('ascii'))

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task

            elif reason == 'write':
                to_write[sock] = task
        except StopIteration:
            pass


tasks.append(server())
event_loop()

