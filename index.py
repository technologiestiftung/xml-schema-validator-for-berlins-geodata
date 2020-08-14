from xml_validator import validation


# set schema and xml file as parameters
schema_name = 'Brunnen' # under construction: schema name will be input by user from list of schema names (drop-down-menue)
xml = 'testfiles/brunnen_valid.gml' # under construction: xml input by user, either as an file upload or an pasted text

# perform validation
message = validation(schema_name, xml)
print(message)