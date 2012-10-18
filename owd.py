import urllib2, xmltodict
from xml.dom import minidom

CLIENT_ID = 123
CLIENT_AUTH = "abcefeafewaf"

def owd(xml_str, debug=False):
    post = '''<OWD_API_REQUEST api_version="1.0"
          		client_id="%s"
          		client_authorization="%s"
          		testing="FALSE" >%s</OWD_API_REQUEST>''' % (CLIENT_ID, CLIENT_AUTH, xml_str)
    
    url = "https://secure.owd.com/api/api.jsp"

    req = urllib2.Request(url=url, 
            data=post, 
            headers={'Content-Type': 'application/xml'})
    f = urllib2.urlopen(req)
    
    result = f.read()
    if(debug):
        print "Response: \n" + minidom.parseString(result).toprettyxml()
    return xmltodict.parse(result)["OWD_API_RESPONSE"]
    

def find_order(id, debug=False):
    try:
        return owd('''
            <OWD_ORDER_STATUS_REQUEST prefixSearch='TRUE' clientOrderId="''' + id + '''">
            </OWD_ORDER_STATUS_REQUEST>
        ''', debug)
    except Exception as e:
        print "ERROR: EXCEPTION FROM OWD FOR ORDER #*" + id + "*: " + str(e)
        return None;


if __name__ == "__main__":
    print find_order("298290", debug=True)