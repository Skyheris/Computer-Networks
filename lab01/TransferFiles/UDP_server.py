import socket

localIP = "172.17.0.2" # container addr
localPort  = 20001
bufferSize = 2048

msgFromServer  = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

 # Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 # Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

 # Listen for incoming datagrams
bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

filename = bytesAddressPair[0].decode()
address = bytesAddressPair[1]

print("RECEBIDO!")
with open(filename, "rb") as file:
    while True:
        
        chunk = file.read(bufferSize)
        
        if not chunk:
            break
        
        UDPServerSocket.sendto(chunk, address)

UDPServerSocket.close()
