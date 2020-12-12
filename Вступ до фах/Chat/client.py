import sys
import socket

if len(sys.argv) < 3:
    port = 1234
    ip = "127.0.0.1"
else:
    port = int(sys.argv[1])
    ip = sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip,port))
while True:
    sock.send(input("Type here> ").encode('utf-8'))
    print(str.join('',['-' for i in range(20)]))
    print(sock.recv(1024).decode('utf-8'))    
    print(str.join('',['-' for i in range(20)]))