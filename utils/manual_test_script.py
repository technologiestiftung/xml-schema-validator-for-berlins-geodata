from lxml import etree
import os
import time

parsed = etree.parse('./utils/schemas/Brunnen.xsd')
# print(parsed)
schema = etree.XMLSchema(parsed)

xml_string = etree.parse('./utils/testfiles/brunnen_invalid.gml')

previous_elementtag = ''
for elementtag in xml_string.getiterator():
    if previous_elementtag == "{http://www.opengis.net/gml}featureMember":
        elementtag_from_gml = str(elementtag.tag)
        elementtag_from_gml = elementtag_from_gml.replace('{http://ogr.maptools.org/}', '')
        break
    else:
        previous_elementtag = elementtag.tag

body = parsed.xpath("//*[@name='brunnen']")
print(parsed.xpath("//*[@name='brunnen']")[0].attrib['name'])
parsed.xpath("//*[@name='brunnen']")[0].attrib['name'] = elementtag_from_gml
#print(parsed)

#print(body[0].get('name'))
#body.tag = "body-not"

#for e in root.iter('tag_name'):
 #   e.text = "something else" # This works

# for node in parsed.xpath("//*[local-name()='element']"):
#     #update node value with new text 'foo'
#     print(node.name)
#     node.text = 'foo'
   # print ET.tostring(node)

try:
    schema.assertValid(xml_string)
except etree.DocumentInvalid:
    validation_output = 'Die gml-Datei entspricht nicht dem vorgegebenen Schema.\n Gefundene Fehler:\r'
    for error in schema.error_log:
        validation_output = (validation_output + '\n' +
                        "  Line {}: {}".format(error.line, error.message))
       # print(validation_output)
    # save validation success message if xml is valid
else:
    validation_output = 'Die Validierung war erfolgreich. Die gml-Datei entspricht dem vorgegebenen Schema.'
   # print(validation_output)