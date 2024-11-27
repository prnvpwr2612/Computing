import socket

def udp_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode(), (host, port))

    data, _ = client_socket.recvfrom(1024)
    print(f"Received: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()