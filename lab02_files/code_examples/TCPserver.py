#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *
import json

serverPort = 12000
sockBuffer = 2048
dictionary = {}
def main():

    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("172.17.0.2", serverPort))

    serverSocket.listen(1)                      # begin listening for incoming TCP requests
    print("Server is running")

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        number = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes

        if not (1 < number < 100):
            clientSocket.send(json.dumps(dictionary).encode())
main()
