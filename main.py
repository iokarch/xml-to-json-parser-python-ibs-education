import xml.etree.ElementTree as ET
import json

# Пространство имен
XML_NAMESPACES = {"ns1":"ns1:test", "ns2":"ns2:test"}

def getLocalName(tag: str) -> str:
    '''
    Вытаскивает локальное имя ноды
    '''
    namespaces = ["{"+address+"}" for address in XML_NAMESPACES.values()]
    
    for namespace in namespaces:
        if namespace in tag:
            return tag.split(namespace)[1]
    return tag

def convertXmlToJson(xml_data):
    '''
    Конвертирует XML-файл в JSON-файл
    '''

    tree = ET.parse(xml_data)
    root = tree.getroot()

    elements = []

    for element in root.findall("ns1:element", XML_NAMESPACES):
        if getLocalName(element.tag) == 'element':
            json_attr = {}
            
            for child_element in element:
                json_attr[getLocalName(child_element.tag)] = child_element.text

            json_attr['id'] = element.attrib['id']
            elements.append({"element": json_attr})

    json_data = {"elements": elements}

    with open('output.json', 'w') as fp:
        json.dump(json_data, fp, indent=4)

convertXmlToJson("test.xml")