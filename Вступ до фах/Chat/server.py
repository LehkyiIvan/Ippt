import sys
import socket

if len(sys.argv) < 3:
    port = 1234
    ip = "127.0.0.1"
else:
    port = int(sys.argv[1])
    ip = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((ip,port))
sock.listen(10)
message_length = 1024
(client,address) = sock.accept()
while True:
    msg = client.recv(message_length).decode('utf-8')
    print(msg)
    response_for_client = str.format("Message: {0}\nBytes received: {1}\nFrom: {2}",msg,len(msg), address).upper().encode('utf-8')
    client.send(response_for_client)
    

