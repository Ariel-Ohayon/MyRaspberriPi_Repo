import socket

HOST = '192.168.1.48'           # Entering your Address
PORT = 8080                     # 8080 - HTTP Port

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)

print(f'Server Openned on address: {HOST}:{PORT}')

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode('utf-8')
    print(f'HTTP Request: {request}')
    response = f'HTTP/1.1 200 OK \r\nContent-Type: text/html;charset="utf-8"\r\n\r\n'
    print(f'Sending Response: {response}')
    conn.send(response.encode('utf-8'))
    print('GET Request')
    file = open('index.html')
    response = file.read().encode('utf-8')
    file.close()
    conn.send(response)
    print(f'{response.decode("utf-8")}')

