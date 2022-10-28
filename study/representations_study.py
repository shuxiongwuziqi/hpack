from hpack import Encoder

from tool import showByte

e = Encoder()

print("Indexed Header Field Representation")
data = {
    ":method": "GET",
}
huffman = False

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))

print("Literal Header Field with Incremental Indexing - Indexed Name")
data = {
    ":method": "PUSH",
}

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))

print("Literal Header Field with Incremental Indexing - New Name")
data = {
    "custom": "value",
}

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))

print("Literal Header Field Never Indexed -- Indexed Name")
data = [
    ("cookie", "id=1", True)
]

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))

print("Literal Header Field Never Indexed -- New Name")
data = [
    ("custom2", "value2", True)
]

codes = e.encode(data, huffman=huffman)
print(showByte(codes[0]))
