import socket
import struct
import sys
#import takprotobuf
import datetime
import time
import requests
import hashlib
import uuid
import random

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

# Some variables that we need at global scope for the stress tests
numIterations = 0
numSecondsToSleep = 0.0
numUnits = 0
direction = 1.0

while True:

    # prompt the user for the type of message that they want to send
    print('Enter the message type')
    print('XML messages')
    print(' circle                 = cx')
    print(' freeform               = fx')
    print(' geofence               = gx')
    print(' HQ                     = hx')
    print(' marker                 = mx')
    print(' marker iconset         = mix')
    print(' marker spot            = msx')
    print(' range&bearing bullseye = rbbx')
    print(' range&bearing circle   = rbcx')
    print(' range&bearing line     = rblx')
    print(' route                  = rx')
    print(' telestration           = tx')
    print('Protobuf messages')
    print(' HQ                     = hp')
    print('Data Packages')
    print(' send a datapackage     = dpz')
    print('Multi-unit test')
    print(' send multiple units    = nunits')
    print('Exit the program')
    print(' Exit                   = exit')



    messageType = input()

    #try:
    # construct the CoT message
    # construct the time first in the format:
    # 2020-02-08T18:10:44.000Z
    current_time = datetime.datetime.utcnow().isoformat()
    current_time += "Z"
    # this is the time in the future when the message is stale
    days = 10
    seconds = 0
    microseconds = 0
    stale_time = datetime.datetime.utcnow() + datetime.timedelta(days, seconds, microseconds)
    stale_time = stale_time.isoformat() + "Z"
    lat = 43.786
    lon = -74.863
    deltaLat = 0.001
    deltaLon = 0.001
    print(current_time)
    message = ""

    if (messageType == 'cx'):
        # create a circle in xml format
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
        # create a freehand graphic in xml format
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
    elif (messageType == "gx"):
        # create a geofence in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='d0be1c6b-4d86-40ec-bf8f-0e94b621eb3b' type='u-d-c-c' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='38.830898851915514' lon='-77.06586686880725' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <shape>
                        <ellipse major='297.72' minor='297.72' angle='360'/>
                        <link uid='d0be1c6b-4d86-40ec-bf8f-0e94b621eb3b.Style' type='b-x-KmlStyle' relation='p-c'>
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
                    <__geofence elevationMonitored='true' minElevation='-33.30720360300985' monitor='All' trigger='Entry' tracking='true' maxElevation='271.4927963969902' boundingSphere='75000.0'/>
                    <strokeColor value='-1'/>
                    <strokeWeight value='4.0'/>
                    <fillColor value='-1761607681'/>
                    <contact callsign='Geo Fence Circle'/>
                    <remarks></remarks>
                    <archive/>
                    <labels_on value='true'/>
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
    elif (messageType == "msx"):
        # Create a spot marker in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='9405e320-9356-41c4-8449-f46990aa17f8' type='b-m-p-s-m' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-g-i-g-o'>"
        message += "<point lat='38.85606343062312' lon='-77.0563755018233' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <status readiness='true'/>
                    <archive/>
                    <link uid='ANDROID-589520ccfcd20f01' production_time='""" + current_time + "' type='a-f-G-U-C' parent_callsign='HOPE' relation='p-p'/>"
        message += """<contact callsign='R 1'/>
                    <remarks></remarks>
                    <archive/>
                    <color argb='-65536'/>
                    <precisionlocation altsrc='???'/>
                    <usericon iconsetpath='COT_MAPPING_SPOTMAP/b-m-p-s-m/-65536'/>
                </detail>
            </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "rbbx"):
        # Create a range and bearing bullseye in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='4f9c3ccf-7dfc-4ff6-be97-dad745401c5f' type='u-r-b-bullseye' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-g-i-g-o'>"
        message += "<point lat='38.81531363752994' lon='-77.0562908588726' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                    <detail>
                        <archive/>
                        <bullseye mils='false' distance='328.51363744476487' bearingRef='M' bullseyeUID='a64d29da-7cc7-4b64-8f30-5179b542c67b' distanceUnits='m' edgeToCenter='false' rangeRingVisible='false' title='Bullseye 1' hasRangeRings='false'/>
                        <contact callsign='Bullseye 1'/>
                        <remarks></remarks>
                        <archive/>
                        <precisionlocation altsrc='???'/>
                    </detail>
                </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "rbcx"):
        # Create a range and bearing circle in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='9655dd2a-a8ee-4ca0-aae4-ac3c0522e5e5' type='u-r-b-c-c' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='38.817590020847064' lon='-77.04678401125244' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <shape>
                        <ellipse major='468.29991497750774' minor='468.29991497750774' angle='360'/>
                        <link uid='9655dd2a-a8ee-4ca0-aae4-ac3c0522e5e5.Style' type='b-x-KmlStyle' relation='p-c'>
                            <Style>
                                <LineStyle>
                                    <color>ffff0000</color>
                                    <width>3.0</width>
                                </LineStyle>
                                <PolyStyle>
                                    <color>00ff0000</color>
                                </PolyStyle>
                            </Style>
                        </link>
                    </shape>
                    <strokeColor value='-65536'/>
                    <strokeWeight value='3.0'/>
                    <fillColor value='16711680'/>
                    <contact callsign='R&amp;B Circle 1'/>
                    <remarks></remarks>
                    <archive/>
                    <labels_on value='true'/>
                    <precisionlocation altsrc='???'/>
                    <color argb='-65536'/>
                </detail>
            </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "rblx"):
        # Create a range and bearing line in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='58df2fcd-e33e-414f-a718-b18b50cd3137' type='u-rb-a' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='38.82080657998482' lon='-77.05494586670942' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <range value='886.144457943895'/>
                    <bearing value='45.59655671674022'/>
                    <inclination value='0.0'/>
                    <rangeUnits value='1'/>
                    <bearingUnits value='0'/>
                    <northRef value='1'/>
                    <strokeColor value='-65536'/>
                    <strokeWeight value='3.0'/>
                    <contact callsign='R&amp;B 1'/>
                    <remarks></remarks>
                    <archive/>
                    <labels_on value='false'/>
                    <color value='-65536'/>
                </detail>
            </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "rx"):
        # Create a route in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='9017073e-5658-42e7-baa8-b98f3c9c1622' type='b-m-r' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='0.0' lon='0.0' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                <detail>
                    <link uid='f3acf150-d75c-407d-be43-e401ab40fe74' callsign='Route 1 SP' type='b-m-p-w' point='38.84335305982451,-77.05440032542333' remarks='' relation='c'/>
                    <link uid='820ebf04-1300-4c3a-a368-d6f1e21a5ddb' callsign='' type='b-m-p-c' point='38.843641314210366,-77.04564214131744' remarks='' relation='c'/>
                    <link uid='2519b2ce-02f1-4d9b-b4b9-6697adf9c8e8' callsign='' type='b-m-p-c' point='38.84291220017555,-77.04409261643717' remarks='' relation='c'/>
                    <link uid='53788e1b-a9cb-4ce5-95da-73f06a65ceb8' callsign='' type='b-m-p-c' point='38.842996980877274,-77.04170095846979' remarks='' relation='c'/>
                    <link uid='bdb5bd8b-8557-4e8f-ae83-860294db13fc' callsign='' type='b-m-p-c' point='38.841301366842806,-77.04129673458799' remarks='' relation='c'/>
                    <link uid='34f3d30f-84e3-494c-9e8f-d4ffc2e48a15' callsign='' type='b-m-p-c' point='38.84111484929902,-77.03516600571386' remarks='' relation='c'/>
                    <link uid='6378f0c9-32ab-4d32-9339-97039e83f8f5' callsign='' type='b-m-p-c' point='38.84408217385933,-77.03531758966953' remarks='' relation='c'/>
                    <link uid='f6926af1-deec-44f4-ae06-46065c829887' callsign='CP1' type='b-m-p-w' point='38.84657472648999,-77.04057250013307' remarks='' relation='c'/>
                    <link uid='b8c0d16d-149b-4476-835d-7ba1cc78077f' callsign='' type='b-m-p-c' point='38.846744287893436,-77.04963385215032' remarks='' relation='c'/>
                    <link uid='af30287b-0686-48f4-82ea-eb1ef07f6892' callsign='' type='b-m-p-c' point='38.84671037561275,-77.05445085340857' remarks='' relation='c'/>
                    <link uid='9f43ce3a-64bc-4e0a-9ee0-f00f7d920826' callsign='CP2' type='b-m-p-w' point='38.85077984929546,-77.05451822405553' remarks='' relation='c'/>
                    <link uid='e3948985-057c-4186-a46b-f86e9b7527ab' callsign='' type='b-m-p-c' point='38.85042377034823,-77.04973490812077' remarks='' relation='c'/>
                    <link uid='091b1c0b-fbde-4072-8a98-404ca29663a3' callsign='VDO' type='b-m-p-w' point='38.84984726157651,-77.0410272520001' remarks='' relation='c'/>
                    <link_attr planningmethod='Infil' color='-1' method='Driving' prefix='CP' type='Vehicle' stroke='3' direction='Infil' routetype='Primary' order='Ascending Check Points'/>
                    <strokeColor value='-1'/>
                    <strokeWeight value='3.0'/>
                    <__routeinfo>
                        <__navcues/>
                    </__routeinfo>
                    <contact callsign='Route 1'/>
                    <remarks></remarks>
                    <archive/>
                    <labels_on value='false'/>
                    <color value='-1'/>
                </detail>
            </event>"""
        encodedMessage = bytearray(message, 'ascii')
    elif (messageType == "tx"):
        # Create a freehand line (called a "telestration") in xml format
        message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        message += "<event version='2.0' uid='455a0f80-09d1-4088-beb8-ce30cfd34103' type='u-d-f-m' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-e'>"
        message += "<point lat='0.0' lon='0.0' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
        message += """
                    <detail>
                        <link line='&lt;?xml version=&apos;1.0&apos; encoding=&apos;UTF-8&apos; standalone=&apos;yes&apos;?&gt;&lt;event version=&apos;2.0&apos; uid=&apos;741ad148-6d67-43fe-937b-4400cf143dc3&apos; type=&apos;u-d-f&apos; time=&apos;2020-12-16T19:59:34.916Z&apos; start=&apos;2020-12-16T19:59:34.916Z&apos; stale=&apos;2020-12-17T19:59:34.916Z&apos; how=&apos;h-e&apos;&gt;&lt;point lat=&apos;38.83747085261451&apos; lon=&apos;-77.06387615576367&apos; hae=&apos;9999999.0&apos; ce=&apos;9999999.0&apos; le=&apos;9999999.0&apos; /&gt;&lt;detail&gt;&lt;link point=&apos;38.838027634047705,-77.06337210808186&apos;/&gt;&lt;link point=&apos;38.8377981306119,-77.06340377023312&apos;/&gt;&lt;link point=&apos;38.83768019134628,-77.06344493102975&apos;/&gt;&lt;link point=&apos;38.83756543962838,-77.06351458776251&apos;/&gt;&lt;link point=&apos;38.83753356415118,-77.06357157963477&apos;/&gt;&lt;link point=&apos;38.83761644039189,-77.06364440258265&apos;/&gt;&lt;link point=&apos;38.83774075475295,-77.06370139445491&apos;/&gt;&lt;link point=&apos;38.838145573313334,-77.06379004847841&apos;/&gt;&lt;link point=&apos;38.838177448790525,-77.06381854441454&apos;/&gt;&lt;link point=&apos;38.838174261242806,-77.06385337278093&apos;/&gt;&lt;link point=&apos;38.838145573313334,-77.06389136736243&apos;/&gt;&lt;link point=&apos;38.83801169630911,-77.06399901867668&apos;/&gt;&lt;link point=&apos;38.837756692491546,-77.06414466457245&apos;/&gt;&lt;link point=&apos;38.837450687910476,-77.06424914967158&apos;/&gt;&lt;link point=&apos;38.83725305995186,-77.06426498074721&apos;/&gt;&lt;link point=&apos;38.83711280785221,-77.06422381995058&apos;/&gt;&lt;link point=&apos;38.83704905689782,-77.06416999429345&apos;/&gt;&lt;link point=&apos;38.83701718142062,-77.06412250106658&apos;/&gt;&lt;link point=&apos;38.836940680275355,-77.06391036465318&apos;/&gt;&lt;link point=&apos;38.83695024291851,-77.06382171062967&apos;/&gt;&lt;link point=&apos;38.83711599539993,-77.06356841341965&apos;/&gt;&lt;link point=&apos;38.8371446833294,-77.063425933739&apos;/&gt;&lt;link point=&apos;38.8371446833294,-77.0632771216281&apos;/&gt;&lt;link point=&apos;38.837122370495365,-77.06323279461635&apos;/&gt;&lt;link point=&apos;38.83704268180237,-77.06321063111048&apos;/&gt;&lt;link point=&apos;38.836978930847984,-77.06322012975585&apos;/&gt;&lt;link point=&apos;38.83692155498903,-77.06325495812223&apos;/&gt;&lt;link point=&apos;38.83681955346201,-77.06336577565162&apos;/&gt;&lt;link point=&apos;38.836794053080254,-77.06344493102975&apos;/&gt;&lt;link point=&apos;38.83674942741218,-77.0636633998734&apos;/&gt;&lt;link point=&apos;38.836727114578146,-77.06399901867668&apos;/&gt;&lt;link point=&apos;38.83665698852831,-77.06422065373546&apos;/&gt;&lt;link point=&apos;38.836526299071814,-77.0644771171606&apos;/&gt;&lt;link point=&apos;38.8364434228311,-77.06451511174211&apos;/&gt;&lt;link point=&apos;38.83657092473989,-77.0646005995505&apos;/&gt;&lt;link point=&apos;38.836666551171476,-77.0646259292715&apos;/&gt;&lt;link point=&apos;38.836937492727635,-77.06458476847487&apos;/&gt;&lt;link point=&apos;38.83734868638345,-77.0644771171606&apos;/&gt;&lt;link point=&apos;38.837932007616125,-77.06446128608499&apos;/&gt;&lt;link point=&apos;38.837989383475076,-77.06444545500936&apos;/&gt;&lt;link point=&apos;38.83835913901054,-77.06423648481109&apos;/&gt;&lt;link point=&apos;38.83857589225546,-77.06403384704306&apos;/&gt;&lt;link point=&apos;38.83872570699828,-77.06383120927504&apos;/&gt;&lt;link point=&apos;38.83873845718916,-77.06376155254229&apos;/&gt;&lt;link point=&apos;38.838719331902844,-77.06368239716416&apos;/&gt;&lt;link point=&apos;38.8387607700232,-77.06377421740278&apos;/&gt;&lt;strokeColor value=&apos;-1&apos;/&gt;&lt;strokeWeight value=&apos;4.0&apos;/&gt;&lt;contact callsign=&apos;Freehand 1&apos;/&gt;&lt;archive/&gt;&lt;labels_on value=&apos;false&apos;/&gt;&lt;/detail&gt;&lt;/event&gt;'/>
                        <strokeColor value='-1'/>
                        <strokeWeight value='4.0'/>
                        <contact callsign='Freehand 1'/>
                        <remarks> #COA5</remarks>
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
        stale_time = current_time + datetime.timedelta(days, seconds, microseconds)
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

        # add an xmlDetail to the detail
        myDetail.xmlDetail = bytes("<remarks> #COA5</remarks>", 'ascii')

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


        # The header is of the form:
        # <magic byte><protocol type><magic byte>
        # where <magic byte> = \xbf
        # and <protocol type> = \x00 for xml payload (this doesn't work for some reason with WinTAK/ATAK)
        #                       \x01 for protobuf payload (this works with WinTAK/ATAK)
        headerByteArray = bytearray(b'\xbf\x01\xbf')
        takMessageByteArray = bytearray(myTakMessage.SerializeToString())
        encodedMessage = headerByteArray + takMessageByteArray

        print(encodedMessage)
    elif (messageType == "dpz"):
        # Send a pre-canned data package
        # This is the URL of the ATAK Server
        url = 'http://192.168.1.25'
        # This is the location of the zip file that we want to upload
        fileLocation = '/home/tom/Documents/'
        # This is the name of the file that we want to upload
        fileName = 'DP-Plan1.zip'
        # Get the SHA256 hash of this file
        sha256_hash = hashlib.sha256()
        hash = ''
        fullFilename = fileLocation + fileName
        with open(fullFilename,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            print(sha256_hash.hexdigest())
            hash = sha256_hash.hexdigest()
        print ("SHA256 Hash of file " + fullFilename + " = " + hash)


        # First, issue a GET request to set the mission hash
        #  
        getRequest = '/Marti/sync/missionquery'
        #params = {'':}        

        with open('/home/tom/downloads/DP-COA10.zip', 'rb') as f:
            r = requests.post('http://httpbin.org/post', files={'report.xls': f})
       
    elif (messageType == 'nunits'):
        print('Enter the number of units you would like')
        numUnits = int(input())
        print('Enter the number of iterations')
        numIterations = int(input())
        print('Enter the time between updates (seconds)')
        numSecondsToSleep = float(input())

    elif (messageType == "exit"):

        # exit the While loop and the program
        break

    # Send data to the multicast group
    if (messageType != 'nunits'):
        print("message=")
        print(message)
        print("encoded message=")
        print(encodedMessage)

        # only send data once
        sent = sock.sendto(encodedMessage, multicast_group)
    else:
        # Send a bunch of units over and over again, centred around Washington DC
        guidList = list()
        latList = list()
        lonList = list()
        symbolList = list()
        iconsetList = list()
        hashTagList = list()

        # We'll have nunits spread across lonExtent units of llatitude, ongitude (all in a line)
        lonExtent = 1.0
        latExtent = 1.0
        lonDelta = lonExtent/numUnits
        latDelta = latExtent/numUnits

        for i in range(0, numUnits):
            # Create the GUIDs for the objects that we'll send to winTAK
            guidList.append(str(uuid.uuid4()))
            # If you want all the units in a line use this code
            #latList.append(lat + i*latDelta)
            #lonList.append(lon + i*lonDelta)
            # If you want all the units randomly distributed within the area use this code
            latList.append(random.uniform(lat, lat + latExtent))
            lonList.append(random.uniform(lon, lon + lonExtent))

            # There are 4 possible affiliations. f=Friendly, h=Hostile, u=Unknown, n=Neutral
            # cycle through these for every 4th symbol.
            # As well, put a hashtag on each object so that it can be filtered by hashtag in WinTAK
            if ((i%4) == 0):
                # Friendly (f second position)
                symbolList.append('a-f-G-P-U-C-I-Z')
                hashTagList.append('#SA_Friendly')
                iconsetList.append('COT_MAPPING_2525B/a-f/a-f-G-P-U-C-I-Z')
            if ((i%4) == 1):
                # Unknown (u second position)
                symbolList.append('a-u-G-P-U-C-I-Z')
                hashTagList.append('#SA_Unknown')
                iconsetList.append('COT_MAPPING_2525B/a-u/a-u-G-P-U-C-I-Z')
            if ((i%4) == 2):
                # Hostile (h second position)
                symbolList.append('a-h-G-P-U-C-I-Z')
                hashTagList.append('#SA_Hostile')
                iconsetList.append('COT_MAPPING_2525B/a-h/a-h-G-P-U-C-I-Z')
            if ((i%4) == 3):
                # Neutral (n second position)
                symbolList.append('a-n-G-P-U-C-I-Z')
                hashTagList.append('#SA_Neutral')
                iconsetList.append('COT_MAPPING_2525B/a-n/a-n-G-P-U-C-I-Z')

        for i in range(0, numIterations):
            for j in range(0, numUnits):
                current_time = datetime.datetime.utcnow().isoformat()
                current_time += "Z"
                # Create a marker in xml format
                message = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
                message += "<event version='2.0' uid='" + guidList[j] + "' type='" + symbolList[j] + "' time='" + current_time + "' start='" + current_time + "' stale='" + stale_time + "' how='h-g-i-g-o'>"
                message += "<point lat='" + str(latList[j]) + "' lon='" + str(lonList[j]) + "' hae='9999999.0' ce='9999999.0' le='9999999.0' />"
                message += """
                    <detail>
                        <status readiness='true'/>
                        <archive/>
                        <link uid='ANDROID-589520ccfcd20f01' production_time='2020-12-16T19:50:57.629Z' type='a-f-G-U-C' parent_callsign='HOPE' relation='p-p'/>"""
                message += "        <contact callsign='U.16." + str(j) + "'/>"
                message += "        <remarks> " + hashTagList[j] + "</remarks>"
                message += """        <archive/>
                        <color argb='-1'/>
                        <precisionlocation altsrc='???'/>"""
                message += "        <usericon iconsetpath='" + iconsetList[j] + "'/>"
                message += """    </detail>
                </event>"""

                encodedMessage = bytearray(message, 'ascii')
                # send the data
                sent = sock.sendto(encodedMessage, multicast_group)

            # Now, sleep for a bit
            print(' Sent group =' + str(i) + ' sleeping for ' + str(numSecondsToSleep) + ' seconds')
            time.sleep(numSecondsToSleep)

            # And now move the units in a vertical direction. Bounce up and down between lat and latExtent
            numIncrements = 10
            yIncrement = float(latExtent/float(numIncrements))
            for j in range(0, numUnits):
                latList[j] += yIncrement*direction
 
            # reverse direction every numIncrements
            if (((i+1)%numIncrements) == 0):
                direction *= -1.0

print ('closing socket')
sock.close()