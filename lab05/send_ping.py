import socket
import sys
import time

def form_echo_request():
    icmp_header = b'\x08\x00\xe5\xca' # Type of message = 8 Code = 0 | Checksum
    icmp_header += b'\x12\x34\x00\x01' # Identifier = 4660 | Sequence Number = 1
    return icmp_header

def main():
    # Read the number of ping attempts as a program's arg
    n_pings = 1
    i = 1
    dst_IP = ""
    
    if len(sys.argv) < 2:
        print("Wrong number of arguments provided")
        sys.exit(1)
    else:
        dst_IP = sys.argv[1]

    if len(sys.argv) > 2:
        n_pings = int(sys.argv[2])
    
    print("Destination address: ", dst_IP)

    # Create Raw Socket
    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except socket.error as e:
        print('Socket could not be created.')
        print('Error number: ', e.errno)
        sys.exit(1)
    
    # Fill and include IP headers
    sck.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 0)
    
    # Bind socket
    sck.bind(("172.17.0.3",0))

    # Send ICMP echo request spaced by 1 second
    while i <= n_pings:
        i += 1

        # Create the ICMP packet
        icmp_echo_req = form_echo_request()

        sck.sendto(icmp_echo_req, (dst_IP, 2222))
        print("Sent ICMP echo request")
        time.sleep(1)
    
    # Close the socket before exiting
    sck.close()

if __name__ == "__main__":
    main()
