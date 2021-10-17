import socket
import struct
import sys
#import takprotobuf
import datetime
import time

# add the takproto_python directory to your PYTHONPATH.
# This will allow you to import the _pb2 packages.
sys.path.insert(0, './takproto_python')

from takproto_python.contact_pb2 import Contact
from takproto_python.detail_pb2 import Detail
from takproto_python.group_pb2 import Group
from takproto_python.status_pb2 import Status
from takproto_python.takv_pb2 import Takv
from takproto_python.track_pb2 import Track
from takproto_python.takmessage_pb2 import TakMessage
from takproto_python.cotevent_pb2 import CotEvent

def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    millis = (dt - epoch).total_seconds() * 1000.0
    return int(millis)

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

while True:

    # prompt the user for the type of message that they want to send
    print('Enter the message type')
    print('XML messages')
    print(' circle         = cx')
    print(' freeform       = fx')
    print(' HQ             = hx')
    print(' marker         = mx')
    print(' marker iconset = mix')
    print(' telestration   = tx')
    print('Protobuf messages')
    print(' HQ             = hp')
    print('Exit the program')
    print(' Exit           = x')

    messageType = input()

    #try:
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

    if (messageType == 'cx'):
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
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "fx"):
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
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "hx"):
        # Create a Headquarters contact in XML format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='aa0b0312-b5cd-4c2c-bbbc-9c4c70216261' type='a-f-G-E-V-C' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='" + str(lat) + "' lon='" + str(lon) + "' hae='26.767999' ce='9999999.0' le='9999999.0' />"
        message += "<detail><uid Droid='XEliopoli HQ'/><contact callsign='XEliopoli HQ' endpoint='192.168.1.10:4242:tcp'/><__group name='Yellow' role='HQ'/><status battery='100'/><takv platform='WinTAK-CIV' device='LENOVO 20QV0007US' os='Microsoft Windows 10 Home' version='1.10.0.137'/><track speed='0.00000000' course='0.00000000'/></detail>"
        message += "</event>"
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "mx"):
        # Create a marker in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='a0c524c6-0422-4382-9981-e39d1dc71730' type='a-u-G' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-g-i-g-o'>"
        message += "<point lat='38.856650047254725' lon='-77.06364199776728' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <status readiness='true'/>
                    <archive/>
                    <link uid='ANDROID-589520ccfcd20f01' production_time='2020-12-16T19:50:57.629Z' type='a-f-G-U-C' parent_callsign='HOPE' relation='p-p'/>
                    <contact callsign='U.16.135057'/>
                    <remarks></remarks>
                    <archive/>
                    <color argb='-1'/>
                    <precisionlocation altsrc='???'/>
                    <usericon iconsetpath='COT_MAPPING_2525B/a-u/a-u-G'/>
                </detail>
            </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "mix"):
        # Create a marker icon in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='4a0f4f84-240c-4ff9-b7b0-d08beec900b3' type='a-u-G' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-g-i-g-o'>"
        message += "<point lat='38.85513174538468' lon='-77.05143976872927' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                    <detail>
                        <status readiness='true'/>
                        <archive/>
                        <link uid='ANDROID-589520ccfcd20f01' production_time='""" + current_time + "' type='a-f-G-U-C' parent_callsign='HOPE' relation='p-p'/>"
        message += """  <contact callsign='hiker 1'/>
                        <remarks></remarks>
                        <archive/>
                        <color argb='-1'/>
                        <precisionlocation altsrc='???'/>
                        <usericon iconsetpath='f7f71666-8b28-4b57-9fbb-e38e61d33b79/Google/hiker.png'/>
                    </detail>
                </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "tx"):
        # Create a marker icon in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='455a0f80-09d1-4088-beb8-ce30cfd34103' type='u-d-f-m' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='0.0' lon='0.0' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                    <detail>
                        <link line='&lt;?xml version=&apos;1.0&apos; encoding=&apos;UTF-8&apos; standalone=&apos;yes&apos;?&gt;&lt;event version=&apos;2.0&apos; uid=&apos;741ad148-6d67-43fe-937b-4400cf143dc3&apos; type=&apos;u-d-f&apos; time=&apos;2020-12-16T19:59:34.916Z&apos; start=&apos;2020-12-16T19:59:34.916Z&apos; stale=&apos;2020-12-17T19:59:34.916Z&apos; how=&apos;h-e&apos;&gt;&lt;point lat=&apos;38.83747085261451&apos; lon=&apos;-77.06387615576367&apos; hae=&apos;9999999.0&apos; ce=&apos;9999999.0&apos; le=&apos;9999999.0&apos; /&gt;&lt;detail&gt;&lt;link point=&apos;38.838027634047705,-77.06337210808186&apos;/&gt;&lt;link point=&apos;38.8377981306119,-77.06340377023312&apos;/&gt;&lt;link point=&apos;38.83768019134628,-77.06344493102975&apos;/&gt;&lt;link point=&apos;38.83756543962838,-77.06351458776251&apos;/&gt;&lt;link point=&apos;38.83753356415118,-77.06357157963477&apos;/&gt;&lt;link point=&apos;38.83761644039189,-77.06364440258265&apos;/&gt;&lt;link point=&apos;38.83774075475295,-77.06370139445491&apos;/&gt;&lt;link point=&apos;38.838145573313334,-77.06379004847841&apos;/&gt;&lt;link point=&apos;38.838177448790525,-77.06381854441454&apos;/&gt;&lt;link point=&apos;38.838174261242806,-77.06385337278093&apos;/&gt;&lt;link point=&apos;38.838145573313334,-77.06389136736243&apos;/&gt;&lt;link point=&apos;38.83801169630911,-77.06399901867668&apos;/&gt;&lt;link point=&apos;38.837756692491546,-77.06414466457245&apos;/&gt;&lt;link point=&apos;38.837450687910476,-77.06424914967158&apos;/&gt;&lt;link point=&apos;38.83725305995186,-77.06426498074721&apos;/&gt;&lt;link point=&apos;38.83711280785221,-77.06422381995058&apos;/&gt;&lt;link point=&apos;38.83704905689782,-77.06416999429345&apos;/&gt;&lt;link point=&apos;38.83701718142062,-77.06412250106658&apos;/&gt;&lt;link point=&apos;38.836940680275355,-77.06391036465318&apos;/&gt;&lt;link point=&apos;38.83695024291851,-77.06382171062967&apos;/&gt;&lt;link point=&apos;38.83711599539993,-77.06356841341965&apos;/&gt;&lt;link point=&apos;38.8371446833294,-77.063425933739&apos;/&gt;&lt;link point=&apos;38.8371446833294,-77.0632771216281&apos;/&gt;&lt;link point=&apos;38.837122370495365,-77.06323279461635&apos;/&gt;&lt;link point=&apos;38.83704268180237,-77.06321063111048&apos;/&gt;&lt;link point=&apos;38.836978930847984,-77.06322012975585&apos;/&gt;&lt;link point=&apos;38.83692155498903,-77.06325495812223&apos;/&gt;&lt;link point=&apos;38.83681955346201,-77.06336577565162&apos;/&gt;&lt;link point=&apos;38.836794053080254,-77.06344493102975&apos;/&gt;&lt;link point=&apos;38.83674942741218,-77.0636633998734&apos;/&gt;&lt;link point=&apos;38.836727114578146,-77.06399901867668&apos;/&gt;&lt;link point=&apos;38.83665698852831,-77.06422065373546&apos;/&gt;&lt;link point=&apos;38.836526299071814,-77.0644771171606&apos;/&gt;&lt;link point=&apos;38.8364434228311,-77.06451511174211&apos;/&gt;&lt;link point=&apos;38.83657092473989,-77.0646005995505&apos;/&gt;&lt;link point=&apos;38.836666551171476,-77.0646259292715&apos;/&gt;&lt;link point=&apos;38.836937492727635,-77.06458476847487&apos;/&gt;&lt;link point=&apos;38.83734868638345,-77.0644771171606&apos;/&gt;&lt;link point=&apos;38.837932007616125,-77.06446128608499&apos;/&gt;&lt;link point=&apos;38.837989383475076,-77.06444545500936&apos;/&gt;&lt;link point=&apos;38.83835913901054,-77.06423648481109&apos;/&gt;&lt;link point=&apos;38.83857589225546,-77.06403384704306&apos;/&gt;&lt;link point=&apos;38.83872570699828,-77.06383120927504&apos;/&gt;&lt;link point=&apos;38.83873845718916,-77.06376155254229&apos;/&gt;&lt;link point=&apos;38.838719331902844,-77.06368239716416&apos;/&gt;&lt;link point=&apos;38.8387607700232,-77.06377421740278&apos;/&gt;&lt;strokeColor value=&apos;-1&apos;/&gt;&lt;strokeWeight value=&apos;4.0&apos;/&gt;&lt;contact callsign=&apos;Freehand 1&apos;/&gt;&lt;archive/&gt;&lt;labels_on value=&apos;false&apos;/&gt;&lt;/detail&gt;&lt;/event&gt;'/>
                        <strokeColor value='-1'/>
                        <strokeWeight value='4.0'/>
                        <contact callsign='Freehand 1'/>
                        <remarks></remarks>
                        <archive/>
                        <labels_on value='false'/>
                        <color value='-1'/>
                    </detail>
                </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "hp"):
        # Create a protobuf version of the HQ message
        myTakMessage = TakMessage()
        myCotEvent = myTakMessage.cotEvent
        myCotEvent.type = 'a-f-G-E-V-C'
        myCotEvent.uid = 'aa0b0312-b5cd-4c2c-bbbc-9c4c70216261'
        current_time = datetime.datetime.utcnow()
        stale_time = current_time + datetime.timedelta(hours)
        myCotEvent.sendTime = unix_time_millis(current_time)
        myCotEvent.startTime = myCotEvent.sendTime
        myCotEvent.staleTime = unix_time_millis(stale_time)
        myCotEvent.how = 'h-e'
        myCotEvent.lat = lat
        myCotEvent.lon = lon
        myCotEvent.hae = 999999.0
        myCotEvent.ce = 999999.0
        myCotEvent.le = 999999 
        # add a detail to the cot event
        myDetail = myCotEvent.detail

        # add a contact to the detail
        myContact = myDetail.contact
        myContact.endpoint = '192.168.1.10:4242:tcp'
        myContact.callsign = 'PEliopoli HQ'
        
        # add a track to the detail
        myTrack = myDetail.track
        myTrack.speed = 0.0
        myTrack.course = 0.0

        # add a group to the detail
        myGroup = myDetail.group
        myGroup.name = 'Yellow'
        myGroup.role = 'HQ'

        # add a status to the detail
        myStatus = myDetail.status
        myStatus.battery = 82

        # add a takv to the detail
        myTakv = myDetail.takv
        myTakv.device = 'LENOVO 20QV0007US'
        myTakv.platform = 'WinTAK-CIV'
        myTakv.os = 'Microsoft Windows 10 Home'
        myTakv.version = '1.10.0.137'

        headerByteArray = bytearray(b'\xbf\x01\xbf')
        takMessageByteArray = bytearray(myTakMessage.SerializeToString())
        encodedMessage = headerByteArray + takMessageByteArray

        print(encodedMessage)

    elif (messageType == "x"):
        # exit the While loop and the program
        break

    print("message=")
    print(message)
    print("encoded message=")
    print(encodedMessage)

    """     if (messageEcoding == "x"):
            print("Sending the message as xml")
            # The header is of the form:
            # <magic byte><protocol type><magic byte>
            # where <magic byte> = \xbf
            # and <protocol type> = \x00 for xml payload
            #                       \x01 for protobuf payload
            #
            # Since this is xml payload we set the <protocol type> = \x00
            #xmlHeader = b'\xbf\x00\xbf'
            #encodedMessage = bytearray(message, 'utf8')
            encodedMessage = bytearray(message, 'ascii')
            #encodedMessage = xmlHeader + bytes(encodedMessage)
            print("encoded xml message")
            print(encodedMessage)
        else:
            print("Sending the message as protobuf")
            # Now encode the message as protobuf
            decodedMessage = ""
            #encodedMessage = takprotobuf.xmlToProto(message)
            #decodedMessage = takprotobuf.parseProto(encodedMessage)
            print("encoded protobuf message")
            print(encodedMessage)
            #print ('sending "%s"' % decodedMessage) """

    # Send data to the multicast group

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

#finally:

print ('closing socket')
sock.close()