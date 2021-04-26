from iota import Iota, TryteString, ProposedTransaction, Address, Tag
import codecs
import zlib

from iota.transaction.types import TransactionTrytes

# IOTA CONF - INTRODUCE TAIL_TRANS
api = Iota('https://nodes.thetangle.org:443')
tail_transaction = 'DLOXEGLGBWWLFYLPKEIWGHC9UMNJBQOUXJSXEWJTLWI9LNTGQRFNYGUMYNUTOCVLEMXQSAOVGRNIA9999'

# ADJUSTING QUERY - CHANGE
data_size = 5696
bundle = Iota.get_bundles(api,tail_transaction)
trytes = bundle['bundles'][0].as_json_compatible()
total = TransactionTrytes(b'')
for i in trytes:
    total += i['signature_message_fragment']
file = TryteString.encode(total[2673:2673+data_size])

# CREATING FILE
decompressed = zlib.decompress(file)
bPDFout=codecs.decode(decompressed, 'base64')
datafile=open("1.txt",'wb')
datafile.write(bPDFout)
datafile.close()