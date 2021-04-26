from iota import Iota, TryteString, ProposedTransaction, Address, Tag
import codecs
import zlib

# IOTA API CONNECTION. 
api = Iota('https://nodes.thetangle.org:443')
address = ['WRIIHMSNYATYRNRWLLPTANKPYAGHIOWKFYSWOPCZMQIEAFQVWJKVMOSOAFGVOOBGUJIBNVFQAPFQXIO9D']
tag = ['DIVULGACION']

#FILE 
f = open("0.txt", "rb")
pdfdatab=f.read()
f.close()

#ENCODE
b64PDF = codecs.encode(pdfdatab, 'base64')

#COMPRESS
compressed = zlib.compress(b64PDF,9)

# CREATE TRANSACTION
message = [TryteString.from_bytes(compressed)]
print('Data size:', len(message[0]))

tx = ProposedTransaction(
    address = Address(address[0]),
    message = message[0],
    value = 0,
    tag = Tag(tag[0])
)

result = api.send_transfer(transfers=[tx])

print('Transacción enviada correctamente')
print('Tail_transaction:', result['bundle'].tail_transaction.hash)




