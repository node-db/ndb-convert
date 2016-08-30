#coding=utf-8

'''
Convert ndb

@author: Huiyugeng
'''


import json
import py_xml

def xml2json(xml):
    try:
        obj = py_xml.parse_string(xml)
        if obj is not None:
            return json.dumps(obj)
    except:
        pass
    return None

def json2xml(json):
    try:
        obj = json.loads(json)
        if obj is not None:
            return  py_xml.to_xml(obj)
    except:
        pass
    return None

def convert(ndb, script):
    return ndb

