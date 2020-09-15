from utils.xml_validator import validation
from http.server import BaseHTTPRequestHandler
import json
import os
import cgi


class handler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        """ Sets headers required for CORS """
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers",
                         "x-api-key,Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })

        xml = form.getvalue('txt')

        try:
            schema_name = form.getvalue('schemas')
            message = validation(schema_name, xml)
        except:
            message = {"status": "error",
                       "message": 'Keine Datei zum Validieren oder ungültige Datei. Laden Sie entweder eine Datei hoch oder kopieren Sie die GML-Datei in das Textfeld.'}

        # Begin the response
        self.send_response(201)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        data = message

        self.wfile.write(bytes(json.dumps(data), "utf-8"))
        return
