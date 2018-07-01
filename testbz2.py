import bz2
import sys

with open(sys.argv[1], "rb") as f:
    cdata = f.read()
print("Compressed data: %dB" % (len(cdata),))

dec = bz2.BZ2Decompressor()
out = dec.decompress(cdata)
size1 = len(out)
assert not out.strip(b"\0")
assert getattr(dec, "eof", True)
print("Uncompressed OK with bz2.BZ2Decompressor [size: %d B]" % (size1,))

out = None

out = bz2.decompress(cdata)
size2 = len(out)
assert not out.strip(b"\0")
print("Uncompressed OK with bz2.decompress() [size: %d B]" % (size2,))

assert size1 == size2
