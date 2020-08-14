from lxml import etree

def validation(schema_name, xml):
    """
    Validate an XML by an XML-Schema(XSD).

        Parameters:
            schema_name (str): Name of schema. Schemas must be stored in the schema directory as .xsd-files
            xml (str): Path to the XML-File.
        Returns:
            validation_output (str): Formated string that contains validation success massage or error messages.
    """
    # load schema
    schema = etree.XMLSchema(etree.parse('schemas/'+schema_name+'.xsd'))
    # perform validation
    try:
        schema.assertValid(etree.parse(xml))
    # save formated error messages if xml is invalid
    except etree.DocumentInvalid:
        validation_output = 'Die gml-Datei entspricht nicht dem vorgegebenen Schema.\n Gefundene Fehler:\r'
        for error in schema.error_log:
            validation_output = (validation_output + '\n' + "  Line {}: {}".format(error.line, error.message))
    # save validation success message if xml is valid
    else:
        validation_output = 'Die Validierung wurde erfolgreich durchgeführt. Die gml-Datei entspricht dem vorgegebenen Schema.'

    return validation_output