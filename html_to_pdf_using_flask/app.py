from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert_html_to_pdf", methods=["POST"])
def convert_html_to_pdf():
    html_file = request.files["0"]
    pdf_file = html_file.filename + ".pdf"

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    # pdfkit.from_file(html_file.decode('utf-8'), pdf_file, configuration=config)
    # pdfkit.from_file(html_file.read().decode('utf-8'), pdf_file, configuration=config)
    pdfkit.from_file(r"C:\Users\RUDRAPRASADMOHAPATRA\Desktop\htmlToPdfFlask\templates\app2.html", pdf_file, configuration=config)



    # pdfkit.from_file(html_file, pdf_file, configuration=config)

    return send_file(pdf_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
