#coding=utf-8

'''
Convert ndb

@author: Huiyugeng
'''

import json
import py_xml

def xml2json(xml_str):
    obj = py_xml.parse_string(xml_str)
    if obj is not None:
        return json.dumps(obj)
    return None

def json2xml(json_str):
    obj = json.loads(json_str)
    if obj is not None:
        return  py_xml.to_xml(obj)
    return None

def convert(template, data, in_type = 'xml', out_type = 'json'):
    obj = None
    if in_type == 'xml':
        obj = py_xml.parse_string(data)
    elif in_type == 'json':
        obj = json.loads(data)
        
    
    if obj:
        if out_type == 'xml':
            return py_xml.to_xml(obj)
        elif out_type == 'json':
            return json.dump(obj)
        
    return None

