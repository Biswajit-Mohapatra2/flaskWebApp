from flask import Flask, render_template, request, send_file
from weasyprint import HTML
import tempfile
import logging
import os

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    html_file = request.files['html_file']
    
    if not html_file:
        return 'No file', 400

    filename = html_file.filename
    html_path = os.path.join('uploads', filename)
    html_file.save(html_path)

    try:
        pdf_path = os.path.join('downloads', filename.replace('.html', '.pdf'))
        HTML(html_path).write_pdf(pdf_path)

    except Exception as e:
        print(e)
        return 'Error converting to PDF', 500

    return send_file(pdf_path)

if __name__ == '__main__':
    app.run(debug=True)