import socket
import struct
import sys
import takprotobuf
import datetime

#message = 'very important data'
#multicast_group = ('239.2.3.2', 10000)

multicast_group = ('239.2.3.1', 6969)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 10)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # construct the CoT message
    # construct the time first in the format:
    # 2020-02-08T18:10:44.000Z
    current_time = datetime.datetime.utcnow().isoformat()
    current_time += "Z"
    # this is the time in the future when the message is stale
    hours = 10
    stale_time = datetime.datetime.utcnow() + datetime.timedelta(hours)
    stale_time = stale_time.isoformat() + "Z"
    lat = 43.786
    lon = -74.863
    print(current_time)
    message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
    message += "<event version='2.0' uid='aa0b0312-b5cd-4c2c-bbbc-9c4c70216261' type='a-f-G-E-V-C' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
    message += "<point lat='" + str(lat) + "' lon='" + str(lon) + "' hae='26.767999' ce='9999999.0' le='9999999.0' />"
    message += "<detail><uid Droid='Eliopoli HQ'/><contact callsign='Eliopoli HQ' endpoint='192.168.1.10:4242:tcp'/><__group name='Yellow' role='HQ'/><status battery='100'/><takv platform='WinTAK-CIV' device='LENOVO 20QV0007US' os='Microsoft Windows 10 Home' version='1.10.0.137'/><track speed='0.00000000' course='0.00000000'/></detail>"
    message += "</event>"
    print(message)

    # Now encode the message as protobuf
    encodedMessage = takprotobuf.xmlToProto(message)
    decodedMessage = takprotobuf.parseProto(encodedMessage)

    # Send data to the multicast group
    print(encodedMessage)
    print ('sending "%s"' % decodedMessage)
    #sent = sock.sendto(message.encode('utf-8'), multicast_group)
    sent = sock.sendto(encodedMessage, multicast_group)
    # Look for responses from all recipients
    """ while True:
        print ('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print ('timed out, no more responses')
            break
        else:
            print ('received "%s" from %s' % (data, server)) """

finally:
    print ('closing socket')
    sock.close()