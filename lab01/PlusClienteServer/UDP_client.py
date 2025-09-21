import socket
import json

msgFromClient = input("Digite um número entre 1 e 100: ")
dictionary = {}
dictionary["number"] = msgFromClient 
dictionary["name"] = "Francisco Oliveira"
bytesToSend = str.encode(json.dumps(dictionary))

serverAddressPort   = ("172.17.0.2", 20001) # container addr 
bufferSize = 1024

 # Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send the message to server using the UDP socket created
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)

message = bytesAddressPair[0].decode()
message = json.loads(message) #Transformamos de volta no dicionário
if(message["close"]):
    UDPClientSocket.close() #Ordem de fechar vinda do servidor
else:
    print(f"The server {message["name"]} changed the number field to: {message["number"]}")
    UDPClientSocket.close()



