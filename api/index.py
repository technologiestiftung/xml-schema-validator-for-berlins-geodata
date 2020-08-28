from utils.xml_validator import validation
from http.server import BaseHTTPRequestHandler
import json
import os
import cgi

# set schema and xml file as parameters
# under construction: schema name will be input by user from list of schema names (drop-down-menue)
schema_name = 'Brunnen'
# under construction: xml input by user, either as an file upload or an pasted text
xml = './utils/testfiles/brunnen_valid.gml'

# perform validation


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = validation(schema_name, xml)
       # print(message)
        data = {"message": message}
        response = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode())
        return

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        # check if xml comes from uploaded file or pasted string
        file_check = False
        txt_check = False     
        for field in form.keys():
            field_item = form[field]
            if field_item.filename:
                # The field contains an uploaded file
                file_data = field_item.file.read()
                file_len = len(file_data)
                #print(file_data)
                file_data = file_data.decode("utf-8") 
                xml = file_data
                xml = xml.replace("\n","       ")
                del file_data
                file_check = True
                #self.wfile.write(bytes("file received", "utf-8"))
            if form.getvalue('txt'):
                xml = form.getvalue('txt')
                print(xml)
                txt_check = True

        if file_check and txt_check:
                message = '<p style="font-family: Clan Medium, sans-serif"><b style="color:#E60032">Fehler:</b> Bitte machen Sie nur eine Eingabe. Laden Sie entweder eine Datei hoch <b>oder</b> kopieren Sie die GML-Datei in das Textfeld.'
        else:
            try:
                schema_name = form.getvalue('schemas')
                message = validation(schema_name, xml)
            except:
                message = '<p style="font-family: Clan Medium, sans-serif"><b style="color:#E60032">Fehler:</b> Keine Datei zum validieren oder ungültige Datei. Laden Sie entweder eine Datei hoch <b>oder</b> kopieren Sie die GML-Datei in das Textfeld.'

        

        # Begin the response
        self.send_response(201)
        # self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Echo back information about what was posted in the form
        #for field in form.keys():
          #  field_item = form[field]
          #  print(field)
           # print(field_item)
            # if field_item.filename:
            #     # The field contains an uploaded file
            #     file_data = field_item.file.read()
            #     file_len = len(file_data)
            #     print(file_data)
            #     del file_data
            #     self.wfile.write(bytes("file received", "utf-8"))
            # else:
            #     # Regular form value
            #     print(field, form[field].value)
        self.wfile.write(bytes(message, "utf-8"))
        return
