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
    # save error messages if xml is invalid
    except etree.DocumentInvalid:
        validation_output = {}
        error_removal_list = ['{http://ogr.maptools.org/}']
        error_line_list = []
        report = {}

        for error in schema.error_log:
            if error.line not in error_line_list:
                for text in error_removal_list:
                    cleaned_error_message = error.message.replace(text, "")
                cleaned_error_message = cleaned_error_message.replace(
                    "The element is not 'nillable'.", "This element is missing.")
                report[error.line] = cleaned_error_message
                error_line_list.append(error.line)
        validation_output["status"] = "invalid"
        validation_output["message"] = 'Die GML-Datei ist nicht valide! Sie entspricht nicht dem vorgegebenen Schema.'
        validation_output["report"] = report
    # save validation success message if xml is valid
    else:
        validation_output = {"status": "valid",
                             "message": 'Die Validierung war erfolgreich! Die GML-Datei entspricht dem vorgegebenen Schema. Es wurden keine Fehler gefunden.'}
    print(validation_output)
    return validation_output
