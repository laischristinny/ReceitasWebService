import socket

SERVER_PORT= 8080
SERVER = ''
ADDRESS = (SERVER, SERVER_PORT)
HEADER_HTTP = 'HTTP/1.1 200 OK\r\nContent-Type: ; charset: utf-8\r\n\r\n'

ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_path(msg):
    indice = msg.find('5000/')+6
    path= msg[indice:msg.find(' HTTP/1.1')]
    return path

def handle_client(csocket, caddress):
    print("[NEW CONNECTION] ", caddress, "Connected")

    connected = True

    while connected:

        msg = csocket.recv(1024).decode()
        path = get_path(msg)

        if path== "":
            path= "index.html"
        
        try:
            file = open(path, encoding="utf-8", errors='ignore')

            data = HEADER_HTTP
            data += file.read()

            file.close()

            csocket.send(data.encode())

        except:
            data= "HTTP/1.1 404 \r\nContent-Type: ; charset: utf-8\r\n\r\n"
            csocket.send(data.encode())
        
        connected= False

    csocket.close()

def start():
    ssocket.bind(ADDRESS)
    ssocket.listen()

    print("[LISTENING] Server is listening on ", SERVER)
    while True:
        csocket, caddress = ssocket.accept()
        handle_client(csocket, caddress)

print("[STARTING] The server is starting")
start()