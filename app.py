from flask import Flask, request, render_template, send_file
from docx2pdf import convert

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def convert_word_to_pdf():
    if request.method == "POST":
        # Handle file upload
        uploaded_file = request.files["word_file"]
        if uploaded_file.filename != "":
            # Save the uploaded file to a temporary location
            uploaded_file.save("temp.docx")

            # Convert the Word file to PDF
            convert("temp.docx")

            # Provide a download link for the PDF
            return send_file("temp.pdf", as_attachment=True, download_name="converted.pdf")

    return render_template("index.html")

if __name__ == '__main__':
    # Use Gunicorn as the web server
    import os
    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable provided by Render
    app.run(debug=False, host=host, port=port)
