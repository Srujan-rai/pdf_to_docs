from http.server import SimpleHTTPRequestHandler
import http.server
import socketserver
from pdf2docx import Converter
import shutil

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Save the uploaded PDF file
        with open('uploaded.pdf', 'wb') as pdf_file:
            pdf_file.write(post_data)

        # Convert the PDF to DOCX
        cv = Converter('uploaded.pdf')
        cv.convert('converted.docx', start=0, end=None)
        cv.close()

        # Send the converted DOCX file to the client
        self.send_response(200)
        self.send_header('Content-Disposition', 'attachment; filename=converted.docx')
        self.send_header('Content-type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        self.end_headers()

        with open('converted.docx', 'rb') as docx_file:
            shutil.copyfileobj(docx_file, self.wfile)

if __name__ == '__main__':
    port = 0
    Handler = MyHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()
