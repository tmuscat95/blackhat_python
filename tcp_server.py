import socket
import threading

ip = "127.0.0.1"
port = 3000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ip,3000)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(request)
    client_socket.send("ACK")

    client_socket.close()


while True:
    client,addr = server.accept()

    print addr[0]
    print addr[1]
    
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()