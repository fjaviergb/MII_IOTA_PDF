import codecs
import zlib
import iota_client

# IOTA CONF - INTRODUCE TAIL_TRANS
client = iota_client.Client()
print(client)
message_id = '602a463e1acbe5aadab527f555175e3715bb4ba7daa037c86e7e8987e744cd69'

# ADJUSTING QUERY - CHANGE
file = bytearray(client.get_message_data(message_id)['payload']['indexation'][0]['data'])
print(file)

# CREATING FILE
decompressed = zlib.decompress(file)
bPDFout=codecs.decode(decompressed, 'base64')
datafile=open("1.txt",'wb')
datafile.write(bPDFout)
datafile.close()