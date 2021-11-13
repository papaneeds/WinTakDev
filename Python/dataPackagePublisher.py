import http.client
import pprint
import urllib.parse
import hashlib
import requests
import socket
import datetime
import re

myResponse = '<event version="2.0" uid="GeoChat.SERVER-UID.HUEY.5c97a2e2-4483-11ec-8b80-39af8bf37572" type="b-t-f" how="h-g-i-g-o" start="2021-11-13T13:12:32.671080Z" time="2021-11-13T13:12:32.671068Z" stale="2021-11-13T13:13:32.671087Z"><detail><__chat id="Python-351853091325412" parent="RootContactGroup" chatroom="HUEY" groupOwner="True"><chatgrp uid0="SERVER-UID" uid1="Python-351853091325412" id="Python-351853091325412" /></__chat><link uid="SERVER-UID" relation="p-p" type="a-f-G-U-C-I" /><remarks time="2021-11-13T13:12:32Z" source="SERVER" to="Python-351853091325412">Welcome to FreeTAKServer FreeTAKServer-1.9.1 Public. The Parrot is not dead. It&#8217;s just resting</remarks><__serverdestination /><marti><dest><callsign /></dest><dest /><dest /></marti></detail><point le="9999999.0" ce="9999999.0" hae="9999999.0" lon="0" lat="0" /></event><event version="2.0" uid="GeoChat.SERVER-UID.HUEY.5c97a2e2-4483-11ec-8b80-39af8bf37572" type="b-t-f" how="h-g-i-g-o" start="2021-11-13T13:12:32.671080Z" time="2021-11-13T13:12:32.671068Z" stale="2021-11-13T13:13:32.671087Z"><detail><__chat id="Python-351853091325412" parent="RootContactGroup" chatroom="HUEY" groupOwner="True"><chatgrp uid0="SERVER-UID" uid1="Python-351853091325412" id="Python-351853091325412" /></__chat><link uid="SERVER-UID" relation="p-p" type="a-f-G-U-C-I" /><remarks time="2021-11-13T13:12:32Z" source="SERVER" to="Python-351853091325412">Welcome to FreeTAKServer FreeTAKServer-1.9.1 Public. The Parrot is not dead. It&#8217;s just resting</remarks><__serverdestination /><marti><dest><callsign /></dest><dest /><dest /></marti></detail><point le="9999999.0" ce="9999999.0" hae="9999999.0" lon="0" lat="0" /></event><event version="2.0" uid="GeoChat.SERVER-UID.HUEY.5c97a2e2-4483-11ec-8b80-39af8bf37572" type="b-t-f" how="h-g-i-g-o" start="2021-11-13T13:12:32.671080Z" time="2021-11-13T13:12:32.671068Z" stale="2021-11-13T13:13:32.671087Z"><detail><__chat id="Python-351853091325412" parent="RootContactGroup" chatroom="HUEY" groupOwner="True"><chatgrp uid0="SERVER-UID" uid1="Python-351853091325412" id="Python-351853091325412" /></__chat><link uid="SERVER-UID" relation="p-p" type="a-f-G-U-C-I" /><remarks time="2021-11-13T13:12:32Z" source="SERVER" to="Python-351853091325412">Welcome to FreeTAKServer FreeTAKServer-1.9.1 Public. The Parrot is not dead. It&#8217;s just resting</remarks><__serverdestination /><marti><dest><callsign /></dest><dest /><dest /></marti></detail><point le="'
eventRegexString = r"<event(.*?)<\/event>"
p = re.compile(eventRegexString)
m = p.findall(myResponse)
print(m)
if (len(m) > 0):
    for match in m:
        # Find the time in the string
        timeRegexString = r' time="(.*?)"'
        tp = re.compile(timeRegexString)
        tm = tp.findall(match)
        print(tm)

# This is the URL of the ATAK Server
serverUrl = '127.0.0.1'
serverPort = '8080'

connection = http.client.HTTPConnection(serverUrl, serverPort, timeout=10)

# The next three lines show examples of a get request
requestPath = '/Marti/api/version/config'
#connection.request("GET", requestPath)
#response = connection.getresponse()
#print("Status: {} and reason: {}".format(response.status, response.reason))
#headers = response.getheaders()
#body = response.read()
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint("Headers: {}".format(headers))
#pp.pprint("Body: {}".format(body))

# Let's pretend that we are an ATAK client talking to a TAKServer
# 1. Get the server config info
protocolAndIP = "http://" + serverUrl + ":" + serverPort
response = requests.get(protocolAndIP + requestPath)
print (response.text)

# 2. Get the client endpoints
requestPath = '/Marti/api/clientEndPoints'
response = requests.get(protocolAndIP + requestPath)
print (response.text)

# 3. Let's create the message to send to the TAKServer through
# a socket.

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

message = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
message += '<event version="2.0" uid="Python-351853091325412" type="a-f-G-U-C" time="' + current_time +'" start="' + current_time + '" stale="' + stale_time +'"'
message +=  '  how="m-g"><point lat="' + str(lat) + '" lon="' + str(lon) + '" hae="37.998" ce="15.0" le="9999999.0"/>'
message += '<detail><takv os="28" version="4.4.0.6 (2e7a914b).1632502166-CIV" device="VirtualBox" platform="ATAK-CIV"/>'
message += '<contact endpoint="*:-1:stcp" phone="+16137629401" callsign="HUEY"/><uid Droid="HUEY"/>'
message += '<precisionlocation altsrc="GPS" geopointsrc="GPS"/><__group role="Team Member" name="Cyan"/><status battery="89"/><track course="79.75057107201846" speed="0.0"/></detail></event>'

print ("About to send outbound message")
print (message)

# Now, open a socket to the TAKServer
# In this iteration we will not use TLS, just straight up TCP
takServerIP = '192.168.1.25'
takServerPort = 8087
BUFFER_SIZE = 1024

print("Connecting to TAKServer at IP=" + takServerIP + ":" + str(takServerPort))
print(" with BUFFER_SIZE=" + str(BUFFER_SIZE))
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the TAKServer
s.connect((takServerIP, takServerPort))
encodedMessage = bytearray(message, 'ascii')
s.send(encodedMessage)

# and get the response, in chunks of BUFFER_SIZE
numChunks = 0
while True:
    full_msg = ''
    while True:
        msg = s.recv(BUFFER_SIZE)
        print('Received a chunk of size=' + str(len(msg)))
        if len(msg) <= 0:
            break
        numChunks += 1
        msg_string = msg.decode("utf-8")
        print('Chunk number ' + str(numChunks) + ' =' + msg_string)
        full_msg += msg_string

        # Now, let's pull events off of the reply as they come in.
        # Use a regular expression to do it
        eventRegexString = r"<event(.?)</event>"
        p = re.compile(eventRegexString)
        m = p.findall(full_msg)
        print(m)

    if len(full_msg) > 0:
        print(full_msg)

s.close()



# Now let's do a POST request

# Send a pre-canned data package

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

requestPath = '/Marti/sync/missionupload'
files = {'file': open(fullFilename, 'rb')}

# headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "*/*"}
# This is the UID of the creator of the data package
creatorUid = 'dataPackagePublisher'
params = {'hash': hash, 'filename': fileName, 'creatorUid': creatorUid}

# Try creating the url manually
url = "http://" + serverUrl + ":" + serverPort + requestPath
url = url + "?"
url = url + "hash=" + hash
url = url + "&"
url = url + "filename=" + fileName
url = url + "&"
url = url + "creatorUid=" + creatorUid

response = requests.post(url, files = files)
print (response.text)

if response.status_code == 200:
    print("everthing went okay")
else:
    print("Oh, oh, errors!")


connection.close()
