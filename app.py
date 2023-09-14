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

if __name__ == "__main__":
    app.run(debug=True)
