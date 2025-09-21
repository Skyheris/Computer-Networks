import socket
import sys

msgFromClient = "Hello UDP Server"
filename = sys.argv[1] #Onde está localizado o nome do file
bytesToSend = str.encode(filename) 

serverAddressPort   = ("172.17.0.2", 20001) # container addr 
bufferSize = 2048

 # Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send the message to server using the UDP socket created
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

with open("Dummy.txt", "wb") as file:
    while True:
        data, _ = UDPClientSocket.recvfrom(bufferSize)
        if data == 0:
            break #Acabou o ficheiro ou vinha vazio
        file.write(data)
        if len(data) < bufferSize:
            break #O ficheiro foi totalmente lido
    
UDPClientSocket.close()
