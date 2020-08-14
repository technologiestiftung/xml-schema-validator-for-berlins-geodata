from lxml import etree

def validation(schema, xml):
    try:
        schema.assertValid(etree.parse(xml))
    except etree.DocumentInvalid:
        validation_output = 'Die gml-Datei entspricht nicht dem vorgegebenen Schema.\n Gefundene Fehler:\r'
        for error in schema.error_log:
            validation_output = (validation_output + '\n' + "  Line {}: {}".format(error.line, error.message))
    else:
        validation_output = 'Die Validierung wurde erfolgreich durchgeführt. Die gml-Datei entspricht dem vorgegebenen Schema.'

    return validation_output