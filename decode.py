import lzma as L, base64 as B, re
code = open('records/track_10min_16mb/2026-04-09_SP8192_3LayerRecur_ParResid_QK525_LegalTTT/train_gpt.py').read()
match = re.search(r'b85decode\("(.+?)"\)', code, re.DOTALL)
data = B.b85decode(match.group(1))
decoded = L.decompress(data, format=L.FORMAT_RAW, filters=[{'id': L.FILTER_LZMA2}])
open('train_gpt_decoded.py', 'wb').write(decoded)
print('Done!')