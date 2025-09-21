import socket
import json

localIP     = "172.17.0.2" # container addr
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"


 # Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 # Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

 # Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = json.loads(bytesAddressPair[0].decode())
    address = bytesAddressPair[1]
    serverNumber = 10
    username = message["name"]
    print(f"Hello {username}!")
    userNumber = int(message["number"])
    if( not (1 < userNumber < 100)):
        message["close"] = True
        bytesToSend = str.encode(json.dumps(message))
        UDPServerSocket.sendto(bytesToSend, address)
        UDPServerSocket.close()
        break
    else:
        
        result = userNumber + serverNumber
        print(f"O client digitou {userNumber} e o server {serverNumber}, que somados dá {result}")

        # Sending a reply to client
        message["number"] = serverNumber
        message["name"] = "Sérgio Garrido"
        message["close"] = False
        bytesToSend = str.encode(json.dumps(message))
        UDPServerSocket.sendto(bytesToSend, address)
