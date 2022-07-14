import socket

target_host = "www.microsoft.com"
target_port = 80

# create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # connect the client
    client.connect((target_host, target_port))

    # send some data
    client.send(b"GET /HTTP/1.1\nHost: www.microsoft.com\n\n")

    # recieve some data
    response = client.recv(4096)
    print(response.decode())
