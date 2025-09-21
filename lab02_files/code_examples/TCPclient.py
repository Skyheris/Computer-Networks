#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *

serverName = "172.17.0.2"            # server name
serverPort = 12000                  # socket server port number
sockBuffer = 2048                   # socket buffer size

def main():
    clientSocket = socket(AF_INET,SOCK_STREAM)       # create TCP socket
    clientSocket.connect((serverName, serverPort))   # open TCP connection

    number = input("Input number: ")   # take input

    clientSocket.send(number.encode())             # send user's sentence
                                                     # over TCP connection

    clientSocket.close()            # close TCP connection

main()
