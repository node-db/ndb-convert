#coding=utf-8

import py_xml
import convert

xml = '''
<root>
    <group name="test">
        <family>green</family>
        <family>cooker</family>
        <start/>
    </group>
    <parent name="green">
        <child name="jim" age="23" sex="male">
            <address>Shenzhen</address>
            <phone>18607578001</phone>
        </child>
        <child name="lucy" age="21" sex="female" address="Chongqing">
            <address>Guangzhou</address>
            <phone>18607578002</phone>
        </child>
        <child name="lily" age="21" sex="female">
            <address>Hangzhou</address>
            <phone>18607578003</phone>
        </child>
    </parent>
    <parent name="cooker">
        <child name="tim" age="34" sex="male">
            <address>Beijing</address>
            <phone>13704453232</phone>
        </child>
        <child name="tom" age="45" sex="male">
            <address>Shanghai</address>
            <phone>13391562334</phone>
        </child>
    </parent>
</root>
'''

json = convert.xml2json(xml)
print convert.json2xml(json)

template = '''
<root>
    <child>
        ${root->parent->child->name:lily}
    <child>
</root>
'''

ndb = py_xml.parse_string(xml)
print convert.convert(template, ndb)


