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
    # parse schema and xml
    parsed = etree.parse('./utils/schemas/'+schema_name+'.xsd')
    xml_string = etree.fromstring(xml.encode('utf-8'))

    # find element name from input xml
    previous_elementtag = ''
    for elementtag in xml_string.getiterator():
        if previous_elementtag == "{http://www.opengis.net/gml}featureMember":
            elementtag_from_gml = str(elementtag.tag)
            elementtag_from_gml = elementtag_from_gml.replace('{http://ogr.maptools.org/}', '')
            break
        else:
            previous_elementtag = elementtag.tag

    # replace element name in xsd with element name of xml
    parsed.xpath("//*[@name='"+ schema_name +"']")[0].attrib['name'] = elementtag_from_gml
    schema = etree.XMLSchema(parsed)

    # perform validation
    try:
        schema.assertValid(xml_string)
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
