import socket
import sys
import time
import struct # Used to parse ICMP header

BUFFER_SIZE = 1024

def parse_echo_request(packet):
        icmp_header_bytes = packet[20:28]
        icmp_header = struct.unpack('!BB2sHH', icmp_header_bytes)
        print("ICMP header: ", icmp_header)

def main():

    # Create Raw Socket
    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        print("Socket created")
    except socket.error as e:
        print('Socket could not be created.')
        print('Error number: ', e.errno)
        sys.exit(1)
    
    # Bind socket
    sck.bind(("172.17.0.2",0))

    # Listen for incoming messages
    print("Listening for incoming messages")
    while True:

        # Receive the ICMP packet
        packet, addr = sck.recvfrom(BUFFER_SIZE)

        print("{}B packet received from {}".format(len(packet),addr))
        parse_echo_request(packet)
    
    # Close the socket before exiting
    sck.close()

if __name__ == "__main__":
    main()
