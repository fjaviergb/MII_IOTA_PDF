import codecs
import zlib
import iota_client

# IOTA API CONNECTION. 
client = iota_client.Client()
print(client)

#FILE 
f = open("0.txt", "rb")
pdfdatab=f.read()
f.close()

#ENCODE
b64PDF = codecs.encode(pdfdatab, 'base64')

# CREATE MESSAGE
message = client.message(
    index='COMUNICACIONyDIVULGACION', data=pdfdatab
)
print("Message_ID: {}".format(message['message_id']))




