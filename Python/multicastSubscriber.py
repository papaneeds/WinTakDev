import socket
import struct
import sys
import takprotobuf

# Import the protobuf files (they are in a package which is in the parent directory,
# so I need to add the parent directory to the PYTHONPATH. This is achieved through
# the following two lines)
#import sys
#sys.path.insert(0, '..')

from takproto_python import *  

multicast_group = '239.2.3.1'
server_address = ('', 6969)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#
# Receive/respond loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    
    print ('received %s bytes from %s' % (len(data), address))
    print (data)
    encodedMessage = bytearray(data)
    print ("first byte = " + str(encodedMessage[0]) + ", second byte = " + str(encodedMessage[1]))
    decoded = takprotobuf.parseProto(data)
    print(decoded)

    #print ('sending acknowledgement to', address)
    #sock.sendto('ack'.encode('utf-8'), address)