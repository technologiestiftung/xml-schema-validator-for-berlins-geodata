from lxml import etree
import os


def validation(schema_name, xml):
    """
    Validate an XML by an XML-Schema(XSD).

        Parameters:
            schema_name (str): Name of schema. Schemas must be stored in the schema directory as .xsd-files
            xml (str): XML-File
        Returns:
            validation_output (str): Formated string that contains validation success massage or error messages.
    """
    # load schema
    schema = etree.XMLSchema(etree.parse(
        './utils/schemas/'+schema_name+'.xsd'))
    # perform validation
    try:
        schema.assertValid(etree.fromstring(xml.encode('utf-8')))
    # save formated error messages if xml is invalid
    except etree.DocumentInvalid:
        validation_output = '<p style="font-family: Clan Book, sans-serif"><b style="color:#E60032">Die GML-Datei ist nicht valide!</b><br>Sie entspricht nicht dem vorgegebenen Schema. Folgende Fehler wurden gefunden:</p>'
        error_removal_list = ['{http://ogr.maptools.org/}']
        error_line_list = []
        for error in schema.error_log:
            if error.line not in error_line_list:
                for text in error_removal_list:
                    cleaned_error_message = error.message.replace(text,"")
                validation_output = (validation_output +
                                    '<p style="font-family: Clan Book, sans-serif"><span style="color:#213A8F">Fehler in Zeile {}:</span> {}<br></p>'.format(error.line, cleaned_error_message))
                error_line_list.append(error.line)
    # save validation success message if xml is valid
    else:
        validation_output = '<p style="font-family: Clan Book, sans-serif"><b style="color:#213A8F">Die Validierung war erfolgreich!</b><br> Die GML-Datei entspricht dem vorgegebenen Schema. Es wurden keine Fehler gefunden.</p>'

    return validation_output
