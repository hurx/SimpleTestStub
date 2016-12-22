# -*- coding:utf-8 -*-
import xml.dom.minidom

class CreateResponseXML:

    def get_xml_string(self, file_name):
        demo_file = open(file_name, 'r')
        xml_str = demo_file.read()
        return xml_str

    def createDOM(self, xml_str):
        try:
            xml_str = xml_str.replace('<?xml version="1.0" encoding="GBK"?>', '<?xml version="1.0" encoding="utf-8"?>')
        except:
            pass
        DOMTree = xml.dom.minidom.parseString(xml_str)
        self.collection =  DOMTree.documentElement

    def set_value(self, request_dic):
        items = self.collection.getElementsByTagName('item')
        for item in items:
            name = item.getElementsByTagName('name')[0].childNodes[0].data
            try:
                item.getElementsByTagName('value')[0].childNodes[0].data = request_dic[name]
            except:
                pass

        return '<?xml version="1.0" encoding="GBK"?>\n'+self.collection.toprettyxml()


