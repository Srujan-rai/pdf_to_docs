# PDF to DOCX Converte

## Description
The PDF to DOCX Converter Server is a simple Python script that sets up an HTTP server capable of converting uploaded PDF files into DOCX format. This server uses the `http.server` module for handling HTTP requests and the `pdf2docx` library for the conversion process.which acn be accessed using an website.

## Features
- Converts PDF files to DOCX format via a basic HTTP server.
- Handles file uploads through POST requests.
- Sends the converted DOCX file as an attachment in the HTTP response.

## Requirements
- Python 3.x
- The `pdf2docx` library for PDF to DOCX conversion. You can install it using `pip install pdf2docx`.

## Usage
1. Clone or download this repository to your local machine.

2. Make sure you have Python and the required `pdf2docx` library installed.

3. Run the server using the following command:
   ```bash
   python convert.py
4 . Now go to browser and go to localhost:9600

5. You can also access the hosted website [PDF_TO_DOCX](https://pdf-ti5h.onrender.com/)...

