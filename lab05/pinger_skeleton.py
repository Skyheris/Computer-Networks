from socket import * 
import os
import sys
import struct
import time 
import select 
import array

ICMP_ECHO_REQUEST = 8

# Global variables to compute stats
timeRTT  = []
pkts_snt = 0;
pkts_rcv = 0;

# This function computes the ICMP checksum - You do not need to modify it!
# Impl. inspired by the one found in Scapy's utils.py (Python 3.12)
def checksum_v2(pkt):

    csum = 0                             # Initialize the checksum to all zeros

    if len(pkt) % 2 == 1:   # If the total length is odd, 
        pkt += b"\x00"      # the received data is padded with one octet of zeros

    csum = sum(array.array("H", pkt))    # divide into 16-bits words and sum them
    csum = (csum >> 16) + (csum & 0xffff)
    csum += csum >> 16                   # Handle carry-overs (fold the sum) 
    csum = ~csum                         # invert the sum (one's complement)

    return csum & 0xffff


# Function to receive ICMP echo replies - TODO: FILL THE MISSING SECTIONS
def receiveOnePong(mySocket, ID, timeout, destAddr): 

    global pkts_rcv, timeRTT

    timeLeft = timeout

    while True:

        startedSelect = time.time()
        # Fill in - start

            # Use select to monitor the socket

        #Fill in - end

        howLongInSelect = (time.time() - startedSelect)

        if whatReady[0] == []: # Timeout
            return "0: Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # Fill in - start

            # Fetch the ICMP header from the IP packet

            # Extract timestamp from payload

            # Update stats

            # Return the difference from the sending and receiving time

        # Fill in - end

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "1: Request timed out."

# Function to send ICMP echo requests - TODO: FILL THE MISSING SECTIONS
def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    # Payload is 32-bit time value when the ping packet is created

    global pkts_snt

    # Make a starting header with a 0 checksum
    myChecksum = 0
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)

    # Insert the data into the payload
    data = struct.pack("d", time.time())

    # Calculate the checksum on the data and the header.
    myChecksum = checksum_v2( header + data )

    # Crate the header with the right checksum
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    
    # Fill in - start

        # Prepare and Send the ICMP packet

    # Fill in - end

    pkts_snt += 1

# Starting function - TODO: FILL THE MISSING SECTIONS
def doOnePing(destAddr, timeout):

    # Fill in - start

        # Create the right socket

    # Fill in - end

    # Retrieve the current process ID as ICMP ID value
    myID = os.getpid() & 0xFFFF 

    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePong(mySocket, myID, timeout, destAddr)

    mySocket.close() 
    return delay

def print_stats(host):

    maxRTT = (max(timeRTT) if len(timeRTT) > 0 else 0.0)
    minRTT = (min(timeRTT) if len(timeRTT) > 0 else 0.0)
    avgRTT = float(sum(timeRTT)/len(timeRTT)) if len(timeRTT) > 0 else 0.0
    loss_rate = ((pkts_snt - pkts_rcv)/pkts_snt if pkts_rcv > 0 else '100%')

    print("--- {} Pinger statistics ---".format(host))
    print("{} packets transmitted, {} received, {} packet loss".format(pkts_snt, pkts_rcv, loss_rate))
    print("rtt min/avg/max/ = {:.3f}/{:.3f}/{:.3f} ms".format(minRTT, avgRTT, maxRTT))

def ping(host, timeout=1):

    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Pinger:")
    print("")
    
    try:

        # Send ping requests separated by approximately one second
        while 1 :
            delay = doOnePing(dest, timeout)
            print("RTT ", delay)
            time.sleep(1)

    except KeyboardInterrupt:
        print()
        print_stats(host)

    return delay
    
#sys.argv[1]: IP address of the host to ping
if len(sys.argv) < 2:
    print("[ERROR]Unexpected number of arguments, please try again")
    print("Usage:   pinger IPAddress ")
    print("Example: pinger 172.17.0.2")
    exit(0)
else:
    target_host = sys.argv[1]
    ping(target_host)
