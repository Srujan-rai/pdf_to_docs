from flask import Flask, render_template, request, redirect, url_for, send_file
from docx2pdf import convert
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["doc_file"]
        if uploaded_file.filename != "":

            docx_contents = uploaded_file.read()


            pdf_contents = convert_from_docx(docx_contents)


            return send_pdf(pdf_contents)

    return render_template("index.html")

def convert_from_docx(docx_contents):
    # Create a temporary file to hold the DOCX data
    temp_docx_path = "temp/temp.docx"
    with open(temp_docx_path, "wb") as temp_docx_file:
        temp_docx_file.write(docx_contents)

    # Perform the conversion from DOCX to PDF
    convert(temp_docx_path)

    # Read the converted PDF data
    pdf_contents = None
    with open("temp/temp.pdf", "rb") as pdf_file:
        pdf_contents = pdf_file.read()

    # Clean up temporary files
    os.remove(temp_docx_path)
    os.remove("temp/temp.pdf")

    return pdf_contents

def send_pdf(pdf_contents):
    # Create a BytesIO object from the PDF data
    pdf_file = io.BytesIO(pdf_contents)

    # Provide a download link for the PDF
    return send_file(
        pdf_file,
        as_attachment=True,
        download_name="converted_pdf.pdf",
        mimetype="application/pdf",
    )

if __name__ == '__main__':
    # Use Gunicorn as the web server
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable provided by Render
    app.run(debug=True, host=host, port=port)
