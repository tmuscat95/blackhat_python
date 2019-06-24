import socket;

target_host = "www.google.com"
target_port = 80

#create socket         #ipv4            #TCP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect
client.connect((target_host,target_port))

#send get request
client.sendall("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode("utf-8"))

#receive response
response = client.recv(4096)

print(response)