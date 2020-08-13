from lxml import etree

# schema name will be input by user from list of schema names (drop-down-menue)
schema_name = 'Brunnen'
# load schema, all provided schemas must be stored in the schema directory as .xsd-files
schema = etree.XMLSchema(etree.parse('schemas/'+schema_name+'.xsd'))

# xml input by user, either as an file upload or an pasted text
xml = 'testfiles/brunnen_test.gml'

# perform validation
try:
    schema.assertValid(etree.parse(xml))
except etree.DocumentInvalid:
    message = 'Die gml-Datei entspricht nicht dem vorgegebenen Schema für ' + schema_name +  '-Datensätze.\n Validierungsfehler:\r'
    #for error in schema.error_log:
       # print("  Line {}: {}".format(error.line, error.message[35:]))
else:
    message = 'Die gml-Datei entspricht dem vorgegebenen Schema für ' + schema_name +  '-Datensätze.'