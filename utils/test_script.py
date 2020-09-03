import pickle 
from lxml import etree
import os
import time

parsed = etree.parse('./utils/schemas/Brunnen.xsd')
# print(parsed)
schema = etree.XMLSchema(parsed)

xml_string = etree.parse('./utils/testfiles/brunnen_invalid.gml')
try:
    schema.assertValid(xml_string)
except etree.DocumentInvalid:
    validation_output = 'Die gml-Datei entspricht nicht dem vorgegebenen Schema.\n Gefundene Fehler:\r'
    for error in schema.error_log:
        validation_output = (validation_output + '\n' +
                        "  Line {}: {}".format(error.line, error.message))
        print(validation_output)
    # save validation success message if xml is valid
else:
    validation_output = 'Die Validierung war erfolgreich. Die gml-Datei entspricht dem vorgegebenen Schema.'
    print(validation_output)