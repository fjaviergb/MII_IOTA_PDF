from iota import Iota, TryteString, ProposedTransaction, Address, Tag
import codecs
import zlib

from iota.transaction.types import TransactionTrytes

# IOTA CONF
api = Iota('https://nodes.thetangle.org:443')
seed = 'WVVBOHNRYPONH9GW9BXVAKGGYBULIUPCDVTFSUAFFJP99NTJTGGQRWQCXSWELVDQIRFINIQDMULGEXSWN'
address = ['WRIIHMSNYWKGRNRWLLPTANKPYAGHIOWKFYSWOPCZMQIEAFQVWJKVMOSOAFGVOOBGUJISAZFQAPFQXIO9D']
tag = ['PRUEBADEPDF']
bundle_hash = ['KVHLEYYVZAPQTKTECHAKBVEDNAFLNVMUDJEPYTLVFCZJNLJCEKAZQ9KHEQCLDPT9LXXYZGQCKEI9COEDC']
tail_transaction = 'STSOUKPNZGAEFJTYLXTQBMLYR9JUYMWCRCYEXPTBBBGSSAOKVIODOYZFJTWKGYMIXJEANMQQKVKQ99999'

bundle = Iota.get_bundles(api,tail_transaction)

trytes = bundle['bundles'][0].as_json_compatible()
total = TransactionTrytes(b'')
for i in trytes:
    total += i['signature_message_fragment']
file = TryteString.encode(total[2673:8369])

decompressed = zlib.decompress(file)
bPDFout=codecs.decode(decompressed, 'base64')
datafile=open("C:\\Master\\CUARTO CUATRIMESTRE\\Comunicacion y Divulgacion\\trabajo\\1.txt",'wb')
datafile.write(bPDFout)
datafile.close()