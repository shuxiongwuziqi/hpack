from hpack import Encoder

from tool import showByte

e = Encoder()

data = [
    ("cookie", "id=1", True)
]

print("without huffman")
huffman = False

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))

print("use huffman to encode")
huffman = True

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))
