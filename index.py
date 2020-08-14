from lxml import etree
from xml_validator import validation



# schema name will be input by user from list of schema names (drop-down-menue)
schema_name = 'Brunnen'
# load schema, all provided schemas must be stored in the schema directory as .xsd-files
schema = etree.XMLSchema(etree.parse('schemas/'+schema_name+'.xsd'))

# xml input by user, either as an file upload or an pasted text
xml = 'testfiles/brunnen_invalid.gml'

# perform validation
message = validation(schema, xml)
print(message)