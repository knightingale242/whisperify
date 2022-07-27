import socket #how we are going to connect different instances on the same netork
import threading #how we are going to handle multiple clients

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #IP ADDRESS
print("Current server address:" + SERVER) 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) #binding socket to the address means that anything that connects to this address will hit this socket

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("message recieved".encode(FORMAT))

    conn.close()

    
    pass

def start():
    print(f"[LISTENING] Server is listening on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
