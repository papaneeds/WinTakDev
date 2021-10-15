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

# prompt the user for the type of message that they want to send
print('Enter the message type')
print(' cirlce   = c')
print(' freeform = f')
print(' HQ       = h')
messageType = input()
print('Enter the message encoding')
print(' xml      = x')
print(' protobuf = p')
messageEcoding = input()

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
    deltaLat = 0.001
    deltaLon = 0.001
    print(current_time)
    message = ""

    if (messageType == 'c'):
        lat += deltaLat
        lon += deltaLon
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='6d09b6f6-720a-4eef-a197-183012512316' type='u-d-c-c' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='" + str(lat) + "' lon='" + str(lon) + "' hae='26.767999' ce='9999999.0' le='9999999.0' />"
        message += """
            <detail>
                <shape>
                    <ellipse major='226.98412686380018' minor='226.98412686380018' angle='360'/>
                    <link uid='6d09b6f6-720a-4eef-a197-183012512316.Style' type='b-x-KmlStyle' relation='p-c'>
                        <Style>
                            <LineStyle>
                                <color>ffffffff</color>
                                <width>4.0</width>
                            </LineStyle>
                            <PolyStyle>
                                <color>96ffffff</color>
                            </PolyStyle>
                        </Style>
                    </link>
                </shape>
                <strokeColor value='-1'/>
                <strokeWeight value='4.0'/>
                <fillColor value='-1761607681'/>
                <contact callsign='Drawing Circle 1'/>
                <remarks></remarks>
                <archive/>
                <labels_on value='true'/>
                <precisionlocation altsrc='???'/>
            </detail>
        </event>"""
    elif (messageType == "f"):
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='b112202e-dd33-4fc7-8d3d-09a14e296011' type='u-d-f' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='38.837566759240914' lon='-77.06585180074342' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
            <detail>
                <link point='38.838231810315555,-77.06616468204862'/>
                <link point='38.83745360129687,-77.06579790102278'/>
                <link point='38.83857723982895,-77.06521420648704'/>
                <link point='38.83703273315412,-77.06520237484105'/>
                <link point='38.83676671272426,-77.06643680990649'/>
                <link point='38.83733845812574,-77.06629483015456'/>
                <link point='38.838231810315555,-77.06616468204862'/>
                <strokeColor value='-1'/>
                <strokeWeight value='4.0'/>
                <fillColor value='-1761607681'/>
                <contact callsign='Shape 1'/>
                <remarks></remarks>
                <archive/>
                <labels_on value='false'/>
                <color value='-1'/>
                <precisionlocation altsrc='???'/>
            </detail>
        </event>"""       
    else:
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='aa0b0312-b5cd-4c2c-bbbc-9c4c70216261' type='a-f-G-E-V-C' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='" + str(lat) + "' lon='" + str(lon) + "' hae='26.767999' ce='9999999.0' le='9999999.0' />"
        message += "<detail><uid Droid='Eliopoli HQ'/><contact callsign='Eliopoli HQ' endpoint='192.168.1.10:4242:tcp'/><__group name='Yellow' role='HQ'/><status battery='100'/><takv platform='WinTAK-CIV' device='LENOVO 20QV0007US' os='Microsoft Windows 10 Home' version='1.10.0.137'/><track speed='0.00000000' course='0.00000000'/></detail>"
        message += "</event>"
    print(message)

    if (messageEcoding == "x"):
        print("Sending the message as xml")
        # The header is of the form:
        # <magic byte><protocol type><magic byte>
        # where <magic byte> = \xbf
        # and <protocol type> = \x00 for xml payload
        #                       \x01 for protobuf payload
        #
        # Since this is xml payload we set the <protocol type> = \x00
        xmlHeader = b'\xbf\x00\xbf'
        encodedMessage = bytearray(message, 'utf8')
        encodedMessage = xmlHeader + encodedMessage
        print("encoded xml message")
        print(encodedMessage)
    else:
        print("Sending the message as protobuf")
        # Now encode the message as protobuf
        encodedMessage = takprotobuf.xmlToProto(message)
        decodedMessage = takprotobuf.parseProto(encodedMessage)
        print("encoded protobuf message")
        print(encodedMessage)
        print ('sending "%s"' % decodedMessage)

    # Send data to the multicast group

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