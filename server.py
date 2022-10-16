from distutils.log import debug
from urllib import request

from flask import Flask, request

from src.hpack import Decoder, Encoder, HeaderTuple

PREFIX = "/api/v1"
app = Flask(__name__)

e = Encoder()
d = Decoder()

def showByte(n):
    res = []
    for i in n:
        res.append(bin(i)[2:].zfill(8))
    return res

def toByte(n):
    list = []
    for i in n:
        list.append(int(i, 2))
    return bytearray(list)

def showTable(table):
    table2 = []
    for row in table:
        key, value = row
        table2.append([key.decode('utf-8'), value.decode('utf-8')]) 
    return table2

@app.route(PREFIX+"/encode", methods=["POST"])
def encode():
    json = request.json
    data = json['data']
    huffman = json['huffman']
    codes = e.encode(data, huffman=huffman)
        
    return {
        "code": [showByte(code) for code in codes],
    }

@app.route(PREFIX+"/decode", methods=["POST"])
def decode():
    json = request.json
    data = json['data']
    res = d.decode(toByte(data), raw=False)

    return {
        "res": res,
    }

@app.route(PREFIX+"/table", methods=["POST"])
def table():
    dynamicTable = e.header_table.dynamic_entries
    staticTable = e.header_table.STATIC_TABLE

    return {
        "staticTable": showTable(staticTable),
        "dynamicTable": showTable(dynamicTable),
    }

@app.route(PREFIX+"/clear", methods=["POST"])
def clear():
    size = e.header_table.maxsize
    e.header_table.maxsize = 0
    e.header_table.maxsize = size
    e.header_table.resized = False
    d.header_table.maxsize = 0
    d.header_table.maxsize = size
    d.header_table.resized = False

    return {
        "success": True
    }
