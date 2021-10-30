import http.client
import pprint
import urllib.parse
import hashlib
import requests

# This is the URL of the ATAK Server
serverUrl = '127.0.0.1'
serverPort = '8080'

connection = http.client.HTTPConnection(serverUrl, serverPort, timeout=10)

# The next three lines show examples of a get request
requestPath = '/Marti/api/version'
connection.request("GET", requestPath)
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
headers = response.getheaders()
body = response.read()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))
pp.pprint("Body: {}".format(body))

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
