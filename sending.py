from iota import Iota, TryteString, ProposedTransaction, Address, Tag
import random
import codecs
import zlib

api = Iota('https://nodes.thetangle.org:443')

# SEED CREATED BY PSEUDO-RAND IN PYTHON - NOT SECURE
seed = 'WVVBOHNRYPONH9GW9BXVAKGGYBULIUPCDVTFSUAFFJP99NTJTGGQRWQCXSWELVDQIRFINIQDMULGEXSWN'
address = ['WRIIHMSNYWKGRNRWLLPTANKPYAGHIOWKFYSWOPCZMQIEAFQVWJKVMOSOAFGVOOBGUJISAZFQAPFQXIO9D']
tag = ['PRUEBADEPDFA']


#FILE 
f = open("C:\\Master\\CUARTO CUATRIMESTRE\\Comunicacion y Divulgacion\\trabajo\\0.txt", "rb")
pdfdatab=f.read()
f.close()

#ENCODE
b64PDF = codecs.encode(pdfdatab, 'base64')
# Sb64PDF=b64PDF.decode('utf-8')

#COMPRESS
compressed = zlib.compress(b64PDF,9)
print(len(compressed))

#KEY - https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python
# https://cryptography.io/en/latest/
# https://stuvel.eu/python-rsa-doc/usage.html
# (pubkey, privkey) = rsa.newkeys(2048)
# crypto = rsa.encrypt(b64PDF, pubkey)
# print(crypto)

#LECTURA - https://stackoverflow.com/questions/56230203/converting-a-pdf-file-or-any-binary-to-a-string-in-python-not-grab-text-out-o
#bretdata=Sb64PDF.encode('utf-8')
decompressed = zlib.decompress(compressed)
bPDFout=codecs.decode(b64PDF, 'base64')
datafile=open("C:\\Master\\CUARTO CUATRIMESTRE\\Comunicacion y Divulgacion\\trabajo\\1.txt",'wb')
datafile.write(bPDFout)
datafile.close()

message = [TryteString.from_bytes(compressed)]
print(len(message[0]))

tx = ProposedTransaction(
    address = Address(random.choice(address)),
    message = random.choice(message),
    value = 0,
    tag = Tag(random.choice(tag))
)

result = api.send_transfer(transfers=[tx])

print('Transacción enviada correctamente',
        result['bundle'].tail_transaction.hash,
        result['bundle'].hash)




