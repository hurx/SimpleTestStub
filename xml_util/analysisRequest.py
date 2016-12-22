# -*- coding:utf-8 -*-
import xml.dom.minidom

class AnalysisRequest:
    def __init__(self, xml_str):
        try:
            xml_str = xml_str.replace('<?xml version="1.0" encoding="GBK"?>', '<?xml version="1.0" encoding="utf-8"?>')
        except:
            pass
        DOMTree = xml.dom.minidom.parseString(xml_str)
        self.collection =  DOMTree.documentElement

    def get_request_items(self):
        items = self.collection.getElementsByTagName('item')
        dic = {}
        for item in items:
            name = item.getElementsByTagName('name')[0].childNodes[0].data
            try:
                value = item.getElementsByTagName('value')[0].childNodes[0].data
            except:
                value = ''
            dic[name] = value
        return dic

if __name__ == '__main__':
    file_object = open('request.xml', 'r')
    try:
        file_content = file_object.read()
    finally:
        file_object.close()

    request_xml = AnalysisRequest(file_content)
    request_xml.get_request_items()
