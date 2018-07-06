import base64
from urllib import unquote
from zlib import decompress
from xml.dom import minidom 

def decode(encoded):
  return base64.b64decode(encoded)

def get_xml(compressed_data):
  return decompress(compressed_data)
  
def prettify_xml(string):
  xml = minidom.parseString(string)
  return xml.toprettyxml()
  
def printPareqXML(enc_data):
  decoded = decode(enc_data)
  xml_string = get_xml(decoded)
  print prettify_xml(xml_string)


pareq = raw_input('Enter pareq: ')

printPareqXML(pareq)
