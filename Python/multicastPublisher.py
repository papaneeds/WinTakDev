import socket
import struct
import sys
import takprotobuf
import datetime

#message = 'very important data'
#multicast_group = ('239.2.3.2', 10000)

multicast_group = ('239.2.3.1', 10000)

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
    current_time = datetime.datetime.utcnow().isoformat
    timeString = datetime.strftime("%m/%d/%Y, %H:%M:%S")
    #str(current_time.year) + "-" + str(current_time.month) + "-" + str(current_time.day) + "T" + str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second) + ".000Z"
    print (timeString)
    exit
    message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
    message += "<event version='2.0' uid='aa0b0312-b5cd-4c2c-bbbc-9c4c70216261' type='a-f-G-E-V-C' time='2021-10-11T16:57:44.000Z' start='2020-02-08T18:10:44.000Z' stale='2020-02-08T18:11:11.000Z' how='h-e'>"
    message += "<point lat='43.97957317' lon='-66.07737696' hae='26.767999' ce='9999999.0' le='9999999.0' />"
    message += "<detail><uid Droid='Eliopoli HQ'/><contact callsign='Eliopoli HQ' endpoint='192.168.1.10:4242:tcp'/><__group name='Yellow' role='HQ'/><status battery='100'/><takv platform='WinTAK-CIV' device='LENOVO 20QV0007US' os='Microsoft Windows 10 Home' version='1.10.0.137'/><track speed='0.00000000' course='0.00000000'/></detail>"
    message += "</event>"

    # Send data to the multicast group
    print ('sending "%s"' % message)
    sent = sock.sendto(message.encode('utf-8'), multicast_group)

    # Look for responses from all recipients
    while True:
        print ('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print ('timed out, no more responses')
            break
        else:
            print ('received "%s" from %s' % (data, server))

finally:
    print ('closing socket')
    sock.close()