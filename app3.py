import subprocess
from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

# Specify the full path to the unoconv executable
UNOCONV_PATH = "unoconv"  # Replace with your actual path

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
    # Use unoconv with the specified full path
    process = subprocess.Popen(
        [UNOCONV_PATH, "--stdin", "--stdout", "--format=pdf"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Use text mode for Python 3
    )

    stdout, stderr = process.communicate(input=docx_contents)

    if process.returncode == 0:
        return stdout.encode("utf-8")
    else:
        print("Conversion failed. Error:", stderr)
        return None

def send_pdf(pdf_contents):
    if pdf_contents:
        return send_file(
            io.BytesIO(pdf_contents),
            as_attachment=True,
            download_name="converted_pdf.pdf",
            mimetype="application/pdf",
        )
    else:
        return "Conversion failed."

if __name__ == '__main__':
    # Use Gunicorn as the web server
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable provided by Render
    app.run(debug=True, host=host, port=port)
