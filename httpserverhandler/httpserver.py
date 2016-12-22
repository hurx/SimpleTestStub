# -*-encoding:utf-8-*-
from BaseHTTPServer import BaseHTTPRequestHandler
import urllib
from xml_util.analysisRequest import AnalysisRequest
from xml_util.createResposeXML import CreateResponseXML
import HTMLParser

class HTTPServerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))
        data_str = urllib.unquote(datas).decode("utf-8", 'ignore')
        html_parser = HTMLParser.HTMLParser()
        data_str = html_parser.unescape(data_str)

        request_xml = AnalysisRequest(data_str.encode('utf-8'))
        request_dic = request_xml.get_request_items()

        response_demo = CreateResponseXML()
        if request_dic['type'] == '1':
            xml_str = response_demo.get_xml_string(r'.\xml_util\response1.xml')
        elif request_dic['type'] == '2':
            xml_str = response_demo.get_xml_string(r'.\xml_util\response2.xml')
        else:
            print "not support!"
        response_demo.createDOM(xml_str)
        response_xml = response_demo.set_value(request_dic)

        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(response_xml.encode('utf-8'))